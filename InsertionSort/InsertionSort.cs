
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

void InsertionSort(int[] a)
{
    for (int i = 1; i < a.Length; i++)
    {
        int temp = a[i];
        int j = i - 1;
        while (j >= 0 && temp < a[j])
        {
            a[j + 1] = a[j];
            j = j - 1;

        }
        a[j + 1] = temp;
    }
}

int[] arr = new int[15];
randomnumber(arr);
Console.WriteLine("Array Original: ");
printarray(arr);
InsertionSort(arr);
Console.WriteLine("\nArray Ordenado: ");
printarray(arr);