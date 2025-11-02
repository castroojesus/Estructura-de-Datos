using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.PortableExecutable;

public class SudokuGame
{
    private int[,] grid;
    private int[,] solution;
    private int clues;
    private int vida = 3;
    private int puntos = 0;

    public SudokuGame(string difficulty = "muy facil")
    {
        grid = new int[9, 9];
        solution = new int[9, 9];
        dificultad(difficulty);
        generarsudoku();
    }

    public void dificultad(string difficulty)
    {
        clues = difficulty.ToLower() switch
        {
            "muy facil" => 78,
            "facil" => 78,
            "medio" => 78,
            "dificil"=>78,
            "muy dificil"=>78,
            _ => 44
        };
    }

    public void perdervida()
    {
        vida--;
        if (vida > 0)
        {
            Console.WriteLine($"¡Error! Te quedan {vida} vidas.");
            Console.WriteLine("Presiona cualquier tecla para continuar...");
            Console.ReadKey();
        }
        else
        {
            perderpuntos();
            Console.WriteLine("¡Has perdido todas tus vidas! El juego se reiniciará.");
            Console.WriteLine("Presiona cualquier tecla para continuar...");
            Console.ReadKey();
            
            vida = 3;
        }
    }

    public void ganarpuntos()
    {
        puntos = puntos +500;
        if (puntos >= 0)
        {
            Console.WriteLine($"Has ganado 500 puntos.");
            Console.WriteLine($"Llevas {puntos} puntos.");

        }
    }

    public void ganarpuntospornivel()
    {
        puntos = puntos + 100;
        if (puntos >= 0)
        {
            Console.WriteLine($"Has ganado 100 puntos.");
            Console.WriteLine($"Llevas {puntos} puntos.");

        }
    }

    public void perderpuntos()
    {
        puntos = puntos - 300;
        if (puntos >= 0)
        {
            Console.WriteLine("Has perdido 300 puntos.");
            Console.WriteLine($"Llevas {puntos} puntos.");

        }
    }


    public void generarsudoku()
    {
        Array.Clear(grid, 0, grid.Length);
        Array.Clear(solution, 0, solution.Length);

        if (!llenar(solution))
        {
            throw new Exception("Error al generar la solución del Sudoku.");
        }

        grid = eliminarnumeros(solution, clues);
    }

    private bool llenar(int[,] gridToFill)
    {
        var random = new Random();
        var nums = Enumerable.Range(1, 9).ToList();

        for (int row = 0; row < 9; row++)
        {
            for (int col = 0; col < 9; col++)
            {
                if (gridToFill[row, col] == 0)
                {
                    var shuffledNums = nums.OrderBy(x => random.Next()).ToList();

                    foreach (var num in shuffledNums)
                    {
                        if (lugarvalido(gridToFill, row, col, num))
                        {
                            gridToFill[row, col] = num;

                            if (llenar(gridToFill))
                            {
                                return true;
                            }

                            gridToFill[row, col] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private bool lugarvalido(int[,] gridToCheck, int row, int col, int num)
    {
        // Verifica la fila
        for (int c = 0; c < 9; c++)
        {
            if (gridToCheck[row, c] == num) return false;
        }

        // Verifica la columna
        for (int r = 0; r < 9; r++)
        {
            if (gridToCheck[r, col] == num) return false;
        }

        // Verifica el bloque 3x3
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;

        for (int r = startRow; r < startRow + 3; r++)
        {
            for (int c = startCol; c < startCol + 3; c++)
            {
                if (gridToCheck[r, c] == num) return false;
            }
        }

        return true;
    }

    private int[,] eliminarnumeros(int[,] originalGrid, int cluesCount)
    {
        var puzzle = (int[,])originalGrid.Clone();
        var random = new Random();
        int cellsToRemove = 81 - cluesCount;

        while (cellsToRemove > 0)
        {
            int row = random.Next(0, 9);
            int col = random.Next(0, 9);

            if (puzzle[row, col] != 0)
            {
                puzzle[row, col] = 0;
                cellsToRemove--;
            }
        }

        return puzzle;
    }

    // Propiedades públicas para acceder a los datos
    public int[,] Grid => grid;
    public int[,] Solution => solution;
    public int Clues => clues;

    public void SetCellValue(int row, int col, int value)
    {
        if (row >= 0 && row < 9 && col >= 0 && col < 9)
        {
            grid[row, col] = value;
        }
    }

    public int GetCellValue(int row, int col)
    {
        return grid[row, col];
    }

    public bool validarsolucion(int[,] userGrid)
    {
        for (int row = 0; row < 9; row++)
        {
            for (int col = 0; col < 9; col++)
            {
                if (userGrid[row, col] != solution[row, col])
                {
                    
                    return false;
                }
            }
        }
        return true;
    }

   
}

public class sudoku
{
    private SudokuGame juego;
    
    
    public sudoku(string difficulty="muy facil")
    {
        juego = new SudokuGame(difficulty);
    }

    public void generartablero(int[,] tablero)
    {
        Console.WriteLine("=== SUDOKU ===");
        Console.WriteLine();

        for (int i = 0; i < 9; i++)
        {
            if (i % 3 == 0 && i != 0)
            {
                Console.WriteLine("------+-------+------");
            }

            for (int j = 0; j < 9; j++)
            {
                if (j % 3 == 0 && j != 0)
                {
                    Console.Write("| ");
                }

                int value = tablero[i, j];
                Console.Write(value == 0 ? ". " : $"{value} ");
            }
            Console.WriteLine();
        }
        Console.WriteLine();
    }

    public void jugar()
    {
        var tablerojugador = (int[,])juego.Grid.Clone();
        bool jugando = true;
        int ganado = 0;

        while (jugando)
        {
            Console.Clear();
            Console.WriteLine("Bienvenido a la dificultad MUY FACIL");
            generartablero(tablerojugador);
            Console.WriteLine();
            generartablero(juego.Solution); // Mostrar la solución para depuración

            if (TableroCompleto(tablerojugador))
            {
                if (juego.validarsolucion(tablerojugador))
                {
                    ganado = ganado + 1;

                    Console.WriteLine("¡Felicidades! Avanzas de nivel");
                    juego.ganarpuntospornivel();
                    Console.WriteLine("Presiona cualquier tecla para continuar");
                    
                    Console.ReadKey();

                    // Generar un nuevo tablero cada vez que se gana
                    juego.generarsudoku();
                    tablerojugador = (int[,])juego.Grid.Clone();

                    if (ganado == 2)
                    {
                        
                        Console.WriteLine("¡Has alcanzado el nivel de dificultad FACIL!");
                        juego.ganarpuntos();
                        juego.dificultad("facil");
                        juego.generarsudoku();
                        tablerojugador = (int[,])juego.Grid.Clone();

                        Console.WriteLine("Presiona cualquier tecla para continuar");
                        Console.ReadKey();

                    }
                    else if (ganado == 4)
                    {
                        
                        Console.WriteLine("¡Has alcanzado el nivel de dificultad MEDIO!");
                        juego.ganarpuntos();
                        juego.dificultad("medio");
                        juego.generarsudoku();
                        tablerojugador = (int[,])juego.Grid.Clone();
                        Console.WriteLine("Presiona cualquier tecla para continuar");
                        Console.ReadKey();
                    }
                    else if (ganado == 6)
                    {
                        
                        Console.WriteLine("¡Has alcanzado el nivel de dificultad DIFICIL!");
                        juego.ganarpuntos();
                        juego.dificultad("dificil");
                        juego.generarsudoku();
                        tablerojugador = (int[,])juego.Grid.Clone();
                        Console.WriteLine("Presiona cualquier tecla para continuar");
                        Console.ReadKey();
                    }
                    else if (ganado == 8)
                    {
                        
                        Console.WriteLine("¡Has alcanzado el nivel de dificultad MUY DIFICIL!");
                        juego.ganarpuntos();
                        juego.dificultad("muy dificil");
                        juego.generarsudoku();
                        tablerojugador = (int[,])juego.Grid.Clone();
                        Console.WriteLine("Presiona cualquier tecla para continuar");
                        Console.ReadKey();
                    }
                    else if (ganado == 10)
                    {

                        Console.WriteLine("¡Has completado todos los niveles! ¡Felicidades!");
                        juego.ganarpuntos();
                        Console.WriteLine("Presiona cualquier tecla para continuar");
                        Console.ReadKey();
                        jugando = false;

                    }
                }
            }
            else
            {
                ingresar_numero(tablerojugador);
            }
        }
    }

    private bool TableroCompleto(int[,] tablero)
    {
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                if (tablero[i, j] == 0) // Si encuentra alguna celda vacía
                {
                    return false;
                }
            }
        }
        return true;
    }

    private void ingresar_numero(int[,] userGrid)
    {
        Console.Write("Fila (1-9): ");
        if (!int.TryParse(Console.ReadLine(), out int fila) || fila < 1 || fila > 9)
        {
            Console.WriteLine("Fila no válida.");
            return;
        }

        Console.Write("Columna (1-9): ");
        if (!int.TryParse(Console.ReadLine(), out int columna) || columna < 1 || columna > 9)
        {
            Console.WriteLine("Columna no válida.");
            return;
        }

        Console.Write("Número (1-9): ");
        if (!int.TryParse(Console.ReadLine(), out int numero) || numero < 1 || numero > 9)
        {
            Console.WriteLine("Número no válido.");
            return;
        }

        
        if (userGrid[fila - 1, columna - 1] == 0)
        {
            
            if (juego.Solution[fila - 1, columna - 1] == numero)
            {
                userGrid[fila - 1, columna - 1] = numero;
                
            }
            else
            {
                juego.perdervida();
            }
            return;
        }
        else
        {
            Console.WriteLine("Esta celda ya tiene un número. No se puede modificar.");
            return;
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        bool salir = false;

        while (!salir)
        {
            Console.Clear();
            Console.WriteLine("=== MENÚ PRINCIPAL ===");
            Console.WriteLine("1. Jugar Sudoku");
            Console.WriteLine("2. Salir");
            Console.Write("Selecciona una opción (1-2): ");

            string opcion = Console.ReadLine();

            switch (opcion)
            {
                case "1":
                    var sudokuUI = new sudoku("muy facil");
                    sudokuUI.jugar();  
                    break;
                case "2":
                    salir = true;
                    Console.WriteLine("¡Gracias por jugar! Hasta pronto.");
                    break;
                default:
                    Console.WriteLine("Opción no válida. Presiona cualquier tecla...");
                    Console.ReadKey();
                    break;
            }
        }

        Console.WriteLine("Presiona cualquier tecla para salir completamente.");
        Console.ReadKey();
    }
}        