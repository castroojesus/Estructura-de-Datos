import java.util.Random;

public class BucketSort {

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

public static void insertionSort(int[] bucket) {
    for (int i = 1; i < bucket.length; i++) {
        int key = bucket[i];
        int j = i - 1;
        while (j >= 0 && bucket[j] > key) {
            bucket[j + 1] = bucket[j];
            j = j - 1;
        }
        bucket[j + 1] = key;
    }

    
}
public static void bucketSort(int[] inputArr) {
    int s = inputArr.length;
    int[][] bucketArr = new int[s][0];

    int max_val = Integer.MIN_VALUE;
    for (int num : inputArr) {
        if (num > max_val) {
            max_val = num;
        }
    }

    // Distribuir los elementos en los buckets 
    for (int j : inputArr) {
        double normalized = (double) j / (max_val + 1);
        int bi = (int) (s * normalized);
        if (bi >= s) bi = s - 1; // Asegurar que bi esté dentro de los límites
        int[] newBucket = new int[bucketArr[bi].length + 1];
        System.arraycopy(bucketArr[bi], 0, newBucket, 0, bucketArr[bi].length);
        newBucket[newBucket.length - 1] = j;
        bucketArr[bi] = newBucket;
    }

    // Ordenar cada bucket con insertion sort
    for (int i = 0; i < s; i++) {
        insertionSort(bucketArr[i]);
    }

    // Concatenar los buckets ordenados de nuevo en inputArr
    int idx = 0;
    for (int[] bucket : bucketArr) {
        for (int j : bucket) {
            inputArr[idx] = j;
            idx++;
        }
    }

}
public static void main(String[] args) {
int[] arr=new int[15];
randomnumber(arr);
System.out.println("Arreglo Original: ");
printarray(arr);
bucketSort(arr);
System.out.println("\nArreglo Ordenado: ");
printarray(arr);
}

}
