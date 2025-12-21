using System;

// PILA CON LISTA ENLAZADA
class Node {
    public int data;           // dato del nodo
    public Node next;          // direccion al siguiente nodo
}

class Program {
    static Node top = null;    // puntero a tope de pila
    
    // funcion para insertar en pila
    static void push(int item) {
        Node newNode = new Node();    // crea un nodo
        newNode.data = item;          // asigna el dato
        newNode.next = top;           // el nuevo nodo apunta al anterior tope
        top = newNode;                // el nuevo nodo es ahora el tope
        Console.WriteLine("Elemento insertado: " + item);
    }
    
    // funcion para eliminar un elemento o extraer
    static int pop() {
        if (top == null) {           // si la pila esta vacia
            Console.WriteLine("STACK UNDERFLOW");
            return -1;
        }
        Node temp = top;              // guarda el nodo del tope
        int valor = top.data;         // guarda el dato
        top = top.next;               // mueve el tope al siguiente nodo
        // En C# el recolector de basura maneja la memoria
        return valor;
    }
    
    // funcion para ver el elemento superior 
    static int peek() {
        if (top == null) {           // si esta vacia
            Console.WriteLine("PILA VACIA");
            return -1;
        }
        return top.data;             // retorna el valor del tope
    }
    
    // funcion para ver si la pila esta vacia
    static bool isEmpty() {
        return top == null;          // retorna true si el tope es null, o sea que esta vacia
    }
    
    static void Main() {
        int choice = 0;
        while (choice != 5) {
            Console.WriteLine("\n\n*********Menu Pila*********");
            Console.WriteLine("1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Salir");
            Console.Write("Ingrese su opción: ");
            if (!int.TryParse(Console.ReadLine(), out choice)) {
                choice = 0;
            }
            switch(choice) {
                case 1: {
                    Console.Write("Ingrese el valor a insertar: ");
                    if (int.TryParse(Console.ReadLine(), out int valor)) {
                        push(valor);
                    }
                    break;
                }
                case 2: {
                    int valor = pop();
                    if (valor != -1) Console.WriteLine("Elemento extraído: " + valor);
                    break;
                }
                case 3: {
                    int valor = peek();
                    if (valor != -1) Console.WriteLine("Elemento superior: " + valor);
                    break;
                }
                case 4:
                    Console.WriteLine(isEmpty() ? "La pila está vacía" : "La pila NO está vacía");
                    break;
                case 5:
                    Console.WriteLine("Saliendo del programa...");
                    break;
                default:
                    Console.WriteLine("Por favor, introduzca una opción válida");
                    break;
            }
        }
    }
}