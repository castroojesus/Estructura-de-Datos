using System;

class Program
{
    static void Main()
    {
        int r = 3;
        int c = 3;
        int[] arr = new int[r * c];
        int[,] TwoDArray = new int[,] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        int k = 0;

        for (int x = 0; x < r; x++)
        {
            for (int y = 0; y < c; y++)
            {
                k = x * r + y;
                arr[k] = TwoDArray[x,y];
                k = k + 1;
            }
        }

        Console.WriteLine("Los elementos del array bidimensional son: ");
        for (int x = 0; x < r; x++)
        {
            for (int y = 0; y < c; y++)
            {
                Console.Write(TwoDArray[x,y] + " ");
            }
            Console.WriteLine();
        }

        Console.WriteLine("\nLos elementos del array unidimensional son:");

       for (int x = 0; x < r; x++)
        {
            for (int y = 0; y < c; y++)
            {
                Console.Write(arr[x*r+y]+" " );
            }
            
        }
    }
}
