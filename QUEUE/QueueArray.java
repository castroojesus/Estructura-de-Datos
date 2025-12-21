import java.util.Scanner;

public class QueueArray {
    

    // COLA CON ARRAYS

    static final int MAXSIZE = 5;
    static int[] queue = new int[MAXSIZE];
    static int front = -1, rear = -1;
    
    static void insertar() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el elemento: ");
        int elem = scanner.nextInt();
        
        if (rear == MAXSIZE - 1) {
            System.out.println("OVERFLOW");
            return;
        }
        if (front == -1 && rear == -1) {
            front = rear = 0;
        } else {
            rear++;
        }
        queue[rear] = elem;
        System.out.println("Elemento insertado correctamente");
    }
    
    static void eliminar() {
        if (front == -1 || front > rear) {
            System.out.println("UNDERFLOW");
            return;
        }
        int elemento = queue[front];
        if (front == rear) {
            front = rear = -1;
        } else {
            front++;
        }
        System.out.println("Elemento eliminado " + elemento);
    }
    
    static void mostrar() {
        if (rear == -1 || front == -1 || front > rear) {
            System.out.println("La cola esta vacia");
        } else {
            System.out.println("Elementos de la cola: ");
            for (int i = front; i <= rear; i++) {
                System.out.println(queue[i]);
            }
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opc = 0;
        
        while (opc != 4) {
            System.out.println("\n************************MENU QUEUE****************************");
            System.out.println("==================================================================");
            System.out.println("1. Insertar elemento en la cola");
            System.out.println("2. Eliminar elemento de la cola");
            System.out.println("3. Mostrar la cola");
            System.out.println("4. Salir");
            System.out.print("Ingrese su opcion: ");
            opc = scanner.nextInt();
            
            switch(opc) {
                case 1:
                    insertar();
                    break;
                case 2:
                    eliminar();
                    break;
                case 3:
                    mostrar();
                    break;
                case 4: 
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("\nOpcion invalida. Ingrese de nuevo\n");
            }
        }
        scanner.close();
    }
}

