import java.util.Random;

public class QuickSort {
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

public static void swap(int[] a, int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

public static int partition(int[] a, int low, int high) {
    int pivot = a[high];
    int i = (low - 1);
    for (int j = low; j < high; j++) {
        if (a[j] <= pivot) {
            i++;
            swap(a, i, j);
        }
    }
    swap(a, i + 1, high);
    return i + 1;
}

public static int quickSort(int[] a, int low, int high) {
    if (low < high) {
        int pi = partition(a, low, high);
        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
    return 0;
}

public static void main(String[] args) {
int[] arr=new int[15];
randomnumber(arr);
System.out.println("Arreglo Original: ");
printarray(arr);
quickSort(arr,0,arr.length-1);
System.out.println("\nArreglo Ordenado: ");
printarray(arr);
}

}
