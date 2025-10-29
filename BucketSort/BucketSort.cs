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

    static void insertion_sort(List<int> bucket)
    {
        for (int i = 1; i < bucket.Count; i++)
        {
            int key = bucket[i];
            int j = i - 1;
            while (j >= 0 && bucket[j] > key)
            {
                bucket[j + 1] = bucket[j];
                j = j - 1;
            }
            bucket[j + 1] = key;
        }
    }

    static void bucketSort(int[] inputArr)
    {
        int n = inputArr.Length;
        
        // Crear buckets
        List<int>[] bucketArr = new List<int>[n];
        for (int i = 0; i < n; i++)
        {
            bucketArr[i] = new List<int>();
        }

        // Encontrar el valor máximo para normalización
        int maxVal = 0;
        for (int i = 0; i < n; i++)
        {
            if (inputArr[i] > maxVal)
                maxVal = inputArr[i];
        }

        // Distribuir los elementos en los buckets
        for (int i = 0; i < n; i++)
        {
            // Normalizar al rango [0,1) y calcular índice del bucket
            double normalized = (double)inputArr[i] / (maxVal + 1);
            int bi = (int)(n * normalized);
            
            // Asegurar que el índice esté dentro de los límites
            if (bi >= n) bi = n - 1;
            if (bi < 0) bi = 0;
            
            bucketArr[bi].Add(inputArr[i]);
        }

        // Ordenar cada bucket con insertion sort
        for (int i = 0; i < n; i++)
        {
            if (bucketArr[i].Count > 0)
            {
                insertion_sort(bucketArr[i]);
            }
        }

        // Concatenar los buckets ordenados
        int idx = 0;
        for (int i = 0; i < n; i++)
        {
            foreach (var val in bucketArr[i])
            {
                inputArr[idx++] = val;
            }
        }
    }

    static void Main()
    {
        int[] arr = new int[15];
        randomnumber(arr);
        Console.WriteLine("Array Original: ");
        printarray(arr);
        bucketSort(arr);
        Console.WriteLine("Array Ordenado con Bucket Sort: "); // Corregido el nombre
        printarray(arr);
    }
}
