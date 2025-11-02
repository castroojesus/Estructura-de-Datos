using System;
using System.Collections.Generic;

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
    static void countingSort(int[] arr, int exp)
    {
        int n = arr.Length;
        int[] output = new int[n];
        int[] count = new int[10];

        for (int i = 0; i < n; i++)
            count[(arr[i] / exp) % 10]++;

        for (int i = 1; i < 10; i++)
            count[i] += count[i - 1];

        for (int i = n - 1; i >= 0; i--)
        {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }

        for (int i = 0; i < n; i++)
            arr[i] = output[i];
    }

    static void radix_sort(int[] arr)
    {
        int max = arr[0];
        for (int i = 1; i < arr.Length; i++)
            if (arr[i] > max)
                max = arr[i];

        for (int exp = 1; max / exp > 0; exp *= 10)
            countingSort(arr, exp);
    }
    static void Main()
    {
        int[] arr = new int[15];
        randomnumber(arr);
        Console.WriteLine("Array Original: ");
        printarray(arr);
        radix_sort(arr);
        Console.WriteLine("Array Ordenado con Radix Sort: "); 
        printarray(arr);
    }
}