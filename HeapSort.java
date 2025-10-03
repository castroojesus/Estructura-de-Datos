import java.util.Random;

public class HeapSort {
    
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

public static void heapify(int[] a, int n, int i) {
    int largest = i; 
    int left = 2 * i + 1; 
    int right = 2 * i + 2; 

    if (left < n && a[left] > a[largest])
        largest = left;

    if (right < n && a[right] > a[largest])
        largest = right;

    if (largest != i) {
        int swap = a[i];
        a[i] = a[largest];
        a[largest] = swap;

        heapify(a, n, largest);
    }
}
public static void heapSort(int[] a) {
    int n = a.length;

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(a, n, i);

    for (int i = n - 1; i > 0; i--) {
        int temp = a[0];
        a[0] = a[i];
        a[i] = temp;

        heapify(a, i, 0);
    }
}
public static void main(String[] args) {
int[] arr=new int[15];
randomnumber(arr);
System.out.println("Arreglo Original: ");
printarray(arr);
heapSort(arr);
System.out.println("\nArreglo Ordenado: ");
printarray(arr);
}

}
