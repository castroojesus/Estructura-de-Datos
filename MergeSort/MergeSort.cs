using System;

class Program
{
    static void swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void merge(int[] arr, int left, int mid, int right)
    {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];
        for (int i = 0; i < n1; i++)
            L[i] = arr[left + i];
        for (int j = 0; j < n2; j++)
            R[j] = arr[mid + 1 + j];

        int k = left;
        int i_index = 0, j_index = 0;
        while (i_index < n1 && j_index < n2)
        {
            if (L[i_index] <= R[j_index])
            {
                arr[k] = L[i_index];
                i_index++;
            }
            else
            {
                arr[k] = R[j_index];
                j_index++;
            }
            k++;
        }

        while (i_index < n1)
        {
            arr[k] = L[i_index];
            i_index++;
            k++;
        }

        while (j_index < n2)
        {
            arr[k] = R[j_index];
            j_index++;
            k++;
        }
    }
    static void mergeSort(int[] arr, int left, int right)
    {
        if (left < right)
        {
            int mid = left + (right - left) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }
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

    static void Main()
    {
        int[] arr = new int[15];
        int longitud = arr.Length;
        randomnumber(arr);
        Console.WriteLine("Array Original: ");
        printarray(arr);
        mergeSort(arr, 0, longitud - 1);
        Console.WriteLine("Array Ordenado: ");
        printarray(arr);
    }
}