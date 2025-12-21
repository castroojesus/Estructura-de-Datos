import java.util.Scanner;
public class PilaList {
    

// PILA CON LISTA ENLAZADA
    static class Node {
    int data;           // dato del nodo
    Node next;          // direccion al siguiente nodo
    
    Node() {}
    }


    static Node top = null;    // puntero a tope de pila
    
    // funcion para insertar en pila
    static void push(int item) {
        Node newNode = new Node();    // crea un nodo
        newNode.data = item;          // asigna el dato
        newNode.next = top;           // el nuevo nodo apunta al anterior tope
        top = newNode;                // el nuevo nodo es ahora el tope
        System.out.println("Elemento insertado: " + item);
    }
    
    // funcion para eliminar un elemento o extraer
    static int pop() {
        if (top == null) {           // si la pila esta vacia
            System.out.println("STACK UNDERFLOW");
            return -1;
        }
        Node temp = top;              // guarda el nodo del tope
        int valor = top.data;         // guarda el dato
        top = top.next;               // mueve el tope al siguiente nodo
        temp = null;                  // ayuda al recolector de basura
        return valor;
    }
    
    // funcion para ver el elemento superior 
    static int peek() {
        if (top == null) {           // si esta vacia
            System.out.println("PILA VACIA");
            return -1;
        }
        return top.data;             // retorna el valor del tope
    }
    
    // funcion para ver si la pila esta vacia
    static boolean isEmpty() {
        return top == null;          // retorna true si el tope es null, o sea que esta vacia
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice = 0;
        while (choice != 5) {
            System.out.println("\n\n*********Menu Pila*********");
            System.out.println("1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Salir");
            System.out.print("Ingrese su opción: ");
            try {
                choice = scanner.nextInt();
            } catch (Exception e) {
                scanner.nextLine();
                choice = 0;
            }
            switch(choice) {
                case 1: {
                    System.out.print("Ingrese el valor a insertar: ");
                    int valor = scanner.nextInt();
                    push(valor);
                    break;
                }
                case 2: {
                    int valor = pop();
                    if (valor != -1) System.out.println("Elemento extraído: " + valor);
                    break;
                }
                case 3: {
                    int valor = peek();
                    if (valor != -1) System.out.println("Elemento superior: " + valor);
                    break;
                }
                case 4:
                    System.out.println(isEmpty() ? "La pila está vacía" : "La pila NO está vacía");
                    break;
                case 5:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Por favor, introduzca una opción válida");
            }
        }
        scanner.close();
    }
}

