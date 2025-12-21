import java.util.Scanner;

public class PilaArray {
    

    // PILA

    static final int MAX_SIZE = 100;
    static int[] stack = new int[MAX_SIZE];      // arreglo de la pila
    static int top = -1;                         // elemento del tope de la pila
    
    // funcion para insertar un elemento en la pila
    static void push(int item) {
        if (top == MAX_SIZE - 1) {               // si la pila está llena
            System.out.println("STACK OVERFLOW");
            return;
        }
        stack[++top] = item;                     // incrementa el indice y agrega el elemento a la pila
    }
    
    // funcion para eliminar un elemento o sacar
    static int pop() {
        if (top == -1) {                         // si la pila esta vacia
            System.out.println("STACK UNDERFLOW");
            return -1;
        }
        return stack[top--];
    }
    
    // funcion para ver el elemento superior sin eliminarlo
    static int peek() {
        if (top == -1) {                         // si esta vacia
            System.out.println("PILA VACIA");
            return -1;
        }
        return stack[top];                       // retorna el valor del tope
    }
    
    // funcion para ver si la pila esta vacia
    static boolean isEmpty() {
        return top == -1;                        // retorna true si la pila es -1, o sea que esta vacia 
    }
    
    // funcion para ver si esta llena
    static boolean isFull() {
        return top == MAX_SIZE - 1;              // retorna true si esta llena, si el indice sup es igual al tamaño maximo menos uno
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice = 0;
        while (choice != 6) {
            System.out.println("\n\n*********Menu Pila*********");
            System.out.println("1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Verificar si está llena\n6. Salir");
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
                    System.out.println(isFull() ? "La pila está llena" : "La pila NO está llena");
                    break;
                case 6:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Por favor, introduzca una opción válida");
            }
        }
        scanner.close();
    }
}

