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

    static void heapify(int[] arr, int n, int i)
    {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[left] > arr[largest])
            largest = left;

        if (right < n && arr[right] > arr[largest])
            largest = right;

        if (largest != i)
        {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            heapify(arr, n, largest);
        }
    }

    static void heapSort(int[] arr)
    {
        int n = arr.Length;

        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        for (int i = n - 1; i >= 0; i--)
        {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            heapify(arr, i, 0);
        }
    }

    static void Main()
    {
        int[] arr = new int[15];
        int longitud = arr.Length;
        randomnumber(arr);
        Console.WriteLine("Array Original: ");
        printarray(arr);
        heapSort(arr);
        Console.WriteLine("Array Ordenado con Heap Sort: ");
        printarray(arr);
    }
}
