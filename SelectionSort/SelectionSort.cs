using System;

class Program
{
    static void Main()
    {
        void randomnumber(int[] a)
{
    Random rand = new Random();
    for (int i = 0; i < a.Length; i++)
    {
        a[i] = rand.Next(1, 100);
    }
}

void printarray(int[] a)
{
    for (int i = 0; i < a.Length; i++)
    {
        Console.Write(a[i] + " ");
    }
}

void SelectionSort(int[] a)
{
    for (int i = 0; i < a.Length; i++)
    {
        int small=i;
        for (int j = i + 1; j < a.Length; j++)
        {
           if (a[j]<a[small]){
                small = j;
            }
            int temp = a[small];
            a[small] = a[i];
            a[i] = temp;
        }
    }
}

int[] arr = new int[15];
randomnumber(arr);
Console.WriteLine("Array Original: ");
printarray(arr);
SelectionSort(arr);
Console.WriteLine("\nArray Ordenado: ");
printarray(arr);
    }
}