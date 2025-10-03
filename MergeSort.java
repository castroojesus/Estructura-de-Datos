import java.util.Random;

public class MergeSort {
    
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
public static void merge(int[] a, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int[] L = new int[n1];
    int[] R = new int[n2];

    for (int i = 0; i < n1; i++)
        L[i] = a[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = a[mid + 1 + j];

    int i = 0, j = 0;
    int k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            a[k] = L[i];
            i++;
        } else {
            a[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        a[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        a[k] = R[j];
        j++;
        k++;
    }

}
public static void mergeSort(int[] a, int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;

        mergeSort(a, left, mid);
        mergeSort(a, mid + 1, right);

        merge(a, left, mid, right);
    }
}

public static void main(String[] args) {
int[] arr=new int[15];
randomnumber(arr);
System.out.println("Arreglo Original: ");
printarray(arr);
mergeSort(arr,0,arr.length-1);
System.out.println("\nArreglo Ordenado: ");
printarray(arr);
}

}
