using System;

class Program
{

    static void randomnumber(int[] a)
    {
        Random rand = new Random();
        for (int i = 0; i < a.Length; i++)
        {
            a[i] = rand.Next(1, 100);
        }
    }

    static void printarray(int[] a)
    {
        for (int i = 0; i < a.Length; i++)
        {
            Console.Write(a[i] + " ");
        }
        Console.WriteLine();
    }

    static void shellSort(int[] arr)
    {
        int n = arr.Length;
        for (int gap = n / 2; gap > 0; gap /= 2)
        {
            for (int i = gap; i < n; i++)
            {
                int temp = arr[i];
                int j;
                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                {
                    arr[j] = arr[j - gap];
                }
                arr[j] = temp;
            }
        }
    }

    static void Main()
    {
        int[] arr = new int[15];
        int longitud = arr.Length;
        randomnumber(arr);
        Console.WriteLine("Array Original: ");
        printarray(arr);
        shellSort(arr);
        Console.WriteLine("Array Ordenado con Heap Sort: ");
        printarray(arr);
    }
}
