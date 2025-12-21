using System;

// COLA CON ARRAYS
class Program {
    const int MAXSIZE = 5;
    static int[] queue = new int[MAXSIZE];
    static int front = -1, rear = -1;
    
    static void Insertar() {
        Console.Write("Ingrese el elemento: ");
        string input = Console.ReadLine();
        int elem;
        
        if (!int.TryParse(input, out elem)) {
            Console.WriteLine("Entrada inválida");
            return;
        }
        
        if (rear == MAXSIZE - 1) {
            Console.WriteLine("OVERFLOW");
            return;
        }
        if (front == -1 && rear == -1) {
            front = rear = 0;
        } else {
            rear++;
        }
        queue[rear] = elem;
        Console.WriteLine("Elemento insertado correctamente");
    }
    
    static void Eliminar() {
        if (front == -1 || front > rear) {
            Console.WriteLine("UNDERFLOW");
            return;
        }
        int elemento = queue[front];
        if (front == rear) {
            front = rear = -1;
        } else {
            front++;
        }
        Console.WriteLine("Elemento eliminado " + elemento);
    }
    
    static void Mostrar() {
        if (rear == -1 || front == -1 || front > rear) {
            Console.WriteLine("La cola esta vacia");
        } else {
            Console.WriteLine("Elementos de la cola: ");
            for (int i = front; i <= rear; i++) {
                Console.WriteLine(queue[i]);
            }
        }
    }
    
    static void Main() {
        int opc = 0;
        
        while (opc != 4) {
            Console.WriteLine("\n************************MENU QUEUE****************************");
            Console.WriteLine("==================================================================");
            Console.WriteLine("1. Insertar elemento en la cola");
            Console.WriteLine("2. Eliminar elemento de la cola");
            Console.WriteLine("3. Mostrar la cola");
            Console.WriteLine("4. Salir");
            Console.Write("Ingrese su opcion: ");
            
            if (!int.TryParse(Console.ReadLine(), out opc)) {
                opc = 0;
            }
            
            switch(opc) {
                case 1:
                    Insertar();
                    break;
                case 2:
                    Eliminar();
                    break;
                case 3:
                    Mostrar();
                    break;
                case 4: 
                    Console.WriteLine("Saliendo del programa...");
                    break;
                default:
                    Console.WriteLine("\nOpcion invalida. Ingrese de nuevo\n");
                    break;
            }
        }
    }
}