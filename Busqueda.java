import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] miArray = {1, 2, 3, 4, 5};

        System.out.println("Escriba el índice del elemento que desea buscar (0 a 4):");
        int busqueda = in.nextInt();

        
        if (busqueda < 0 || busqueda >= miArray.length) {
            System.out.println("Error: el índice está fuera del rango del array.");
        } else {
          
            System.out.println("El elemento que se encuentra en el índice " + busqueda + " es: " + miArray[busqueda]);
        }

        in.close(); 
    }
}
