import java.util.Random;

public class SelectionSort {
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

public static void selectionsort(int[] a){
    for (int i = 0; i < a.length; i++)
    {
        int small=i;
        for (int j=i+1;j<a.length;j++){
            if(a[j]<a[small]){
                small=j;
            }
        }
        int temp = a[small];
            a[small] = a[i];
            a[i] = temp;
    }
}

public static void main(String[] args) {
int[] arr=new int[15];
randomnumber(arr);
System.out.println("Arreglo Original: ");
printarray(arr);
selectionsort(arr);
System.out.println("\nArreglo Ordenado: ");
printarray(arr);
}

}
