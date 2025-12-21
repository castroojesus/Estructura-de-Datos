using System;

// PILA
class Program {
    const int MAX_SIZE = 100;
    static int[] stack = new int[MAX_SIZE];      // arreglo de la pila
    static int top = -1;                         // elemento del tope de la pila
    
    // funcion para insertar un elemento en la pila
    static void push(int item) {
        if (top == MAX_SIZE - 1) {               // si la pila está llena
            Console.WriteLine("STACK OVERFLOW");
            return;
        }
        stack[++top] = item;                     // incrementa el indice y agrega el elemento a la pila
    }
    
    // funcion para eliminar un elemento o sacar
    static int pop() {
        if (top == -1) {                         // si la pila esta vacia
            Console.WriteLine("STACK UNDERFLOW");
            return -1;
        }
        return stack[top--];
    }
    
    // funcion para ver el elemento superior sin eliminarlo
    static int peek() {
        if (top == -1) {                         // si esta vacia
            Console.WriteLine("PILA VACIA");
            return -1;
        }
        return stack[top];                       // retorna el valor del tope
    }
    
    // funcion para ver si la pila esta vacia
    static bool isEmpty() {
        return top == -1;                        // retorna true si la pila es -1, o sea que esta vacia 
    }
    
    // funcion para ver si esta llena
    static bool isFull() {
        return top == MAX_SIZE - 1;              // retorna true si esta llena, si el indice sup es igual al tamaño maximo menos uno
    }
    
    static void Main() {
        int choice = 0;
        while (choice != 6) {
            Console.WriteLine("\n\n*********Menu Pila*********");
            Console.WriteLine("1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Verificar si está llena\n6. Salir");
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
                    Console.WriteLine(isFull() ? "La pila está llena" : "La pila NO está llena");
                    break;
                case 6:
                    Console.WriteLine("Saliendo del programa...");
                    break;
                default:
                    Console.WriteLine("Por favor, introduzca una opción válida");
                    break;
            }
        }
    }
}