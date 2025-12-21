
import java.util.Scanner;

public class QueueList {
   

    // Estructura del nodo
    static class Nodo {
        int dato;
        Nodo siguiente;
    }


    static Nodo front = null;
    static Nodo rear = null;
    
    static void insertar() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el elemento: ");
        int elem = scanner.nextInt();
        
        Nodo nuevo = new Nodo();
        nuevo.dato = elem;
        nuevo.siguiente = null;
        
        if (front == null && rear == null) {
            front = rear = nuevo;
        } else {
            rear.siguiente = nuevo;
            rear = nuevo;
        }
        
        System.out.println("Elemento insertado correctamente");
    }
    
    static void eliminar() {
        if (front == null) {
            System.out.println("UNDERFLOW");
            return;
        }
        
        Nodo temp = front;
        int elemento = temp.dato;
        
        front = front.siguiente;
        if (front == null) {
            rear = null;
        }
        
        temp = null; // Ayuda al recolector de basura
        System.out.println("Elemento eliminado: " + elemento);
    }
    
    static void mostrar() {
        if (front == null) {
            System.out.println("La cola está vacía");
            return;
        }
        
        System.out.println("Elementos de la cola:");
        Nodo actual = front;
        while (actual != null) {
            System.out.println(actual.dato);
            actual = actual.siguiente;
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opc = 0;
        
        while (opc != 4) {
            System.out.println("\n*************** MENU QUEUE ***************");
            System.out.println("1. Insertar elemento en la cola");
            System.out.println("2. Eliminar elemento de la cola");
            System.out.println("3. Mostrar la cola");
            System.out.println("4. Salir");
            System.out.print("Ingrese su opción: ");
            opc = scanner.nextInt();
            
            switch (opc) {
                case 1: insertar(); break;
                case 2: eliminar(); break;
                case 3: mostrar(); break;
                case 4: System.out.println("Saliendo del programa..."); break;
                default: System.out.println("Opción inválida. Ingrese de nuevo");
            }
        }
        scanner.close();
    }
}

