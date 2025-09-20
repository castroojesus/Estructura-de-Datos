import java.util.Random;
public class InsertionSort {
    
public static void randomnumber(int[] a){
    Random rand = new Random();
    for (int i=0;i<a.length;i++) {
			a[i]=rand.nextInt(100)+1;
		}
}

public static void printarray(int[] a){
    for (int i=0;i<a.length;i++) {
			System.out.print(a[i]+" ");
		}
}

public static void insertionsort(int[] a){
    for (int i = 1; i < a.length; i++)
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

public static void main(String[] args) {
int[] arr=new int[15];
randomnumber(arr);
System.out.println("Arreglo Original: ");
printarray(arr);
insertionsort(arr);
System.out.println("\nArreglo Ordenado: ");
printarray(arr);
}


}
