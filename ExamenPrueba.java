import java.util.Scanner;
public class ExamenPrueba {
    

	public static void main(String[] args) {
		
		int[] Elementos=new int[10];
		Scanner in = new Scanner(System.in);
		
		
		for(int i=0;i<Elementos.length;i++) {
			
			System.out.println("Ingresa el elemento "+(i+1));
			int numero = in.nextInt();
			Elementos[i]=numero;
			
			
		}
		in.close();
		
		int res=0;
		
		int cont=0;
		
for(int i=0;i<Elementos.length;i++) {
			res=res+Elementos[i];
			
			cont++;
			
		}
double prom=(double)res/cont;

		
		int max=Elementos[0];
		int min = Elementos[0];
		for(int i=0;i<Elementos.length;i++) {
			if(max<Elementos[i]) {
				max=Elementos[i];
			}if(Elementos[i]<min) {
				min=Elementos[i];
			}
		}
		
		System.out.println("Suma de los elementos: "+res);
		System.out.println("Promedio de la suma: "+prom);
		System.out.println("Elemento mayor del arreglo: "+max);
		System.out.println("Elemento menor del arreglo: "+min);

	}	
	

}
