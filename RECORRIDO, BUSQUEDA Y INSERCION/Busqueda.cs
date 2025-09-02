using System;

public class Insercion
{
    public static void Main(string[]args)
    {
        int[] miArray = { 1, 2, 3, 4, 5 };

        Console.WriteLine("Escriba el indice del elemento que desea buscar (0 a 4):");
        int busqueda = int.Parse(Console.ReadLine());

        
        if (busqueda < 0 || busqueda >= miArray.Length)
        {
            Console.WriteLine("Error: el indice esta fuera del rango del array.");
            
        }
        else
        {
            Console.WriteLine("El elemento que se encuentra en el indice " + busqueda + " es: " + miArray[busqueda]);
        }
    }
}
