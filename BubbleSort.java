import java.util.Random;
public class BubbleSort {

	public static void main(String[] args) {
		int []arr=new int[15];
		Random rand = new Random();
		
		for (int i=0;i<arr.length;i++) {
			arr[i]=rand.nextInt(100)+1;
		}
		
		System.out.println("\nArray Original: ");
		for (int i=0;i<arr.length;i++) {
			System.out.print(arr[i]+" ");
		}
		
		int mayor;
		for (int i=0;i<arr.length;i++) {
			for(int j=0;j<arr.length-i-1;j++) {
				
				if(arr[j]>arr[j+1]) {
					mayor=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=mayor;
				}
			}
		}
		System.out.println("\nArray Ordenado: ");
		for (int i=0;i<arr.length;i++) {
			System.out.print(arr[i]+" ");
		}

	}

}

