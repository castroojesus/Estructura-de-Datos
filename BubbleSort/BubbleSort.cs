Random rand = new Random();

int[] arr=new int[15];

for (int i = 0; i < arr.Length; i++)
{
    arr[i] = rand.Next(1, 100);
}
Console.WriteLine("\nArray Original: ");

for (int i = 0; i < arr.Length; i++)
{
    Console.Write(arr[i]+" ");
}

int mayor = 0;
for(int i = 0; i < arr.Length; i++)
{
    for(int j = 0; j < arr.Length - i - 1; j++)
    {
        if (arr[j] > arr[j + 1])
        {
            mayor = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = mayor;
        }
    }
}

Console.WriteLine("\nArray Ordenado: ");

for (int i = 0; i < arr.Length; i++)
{
    Console.Write(arr[i] + " ");
}