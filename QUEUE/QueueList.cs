using System;

// Estructura del nodo
class Nodo {
    public int dato;
    public Nodo siguiente;
}

class Program {
    static Nodo front = null;
    static Nodo rear = null;
    
    static void Insertar() {
        Console.Write("Ingrese el elemento: ");
        string input = Console.ReadLine();
        int elem;
        
        if (!int.TryParse(input, out elem)) {
            Console.WriteLine("Entrada inválida");
            return;
        }
        
        Nodo nuevo = new Nodo();
        nuevo.dato = elem;
        nuevo.siguiente = null;
        
        if (front == null && rear == null) {
            front = rear = nuevo;
        } else {
            rear.siguiente = nuevo;
            rear = nuevo;
        }
        
        Console.WriteLine("Elemento insertado correctamente");
    }
    
    static void Eliminar() {
        if (front == null) {
            Console.WriteLine("UNDERFLOW");
            return;
        }
        
        Nodo temp = front;
        int elemento = temp.dato;
        
        front = front.siguiente;
        if (front == null) {
            rear = null;
        }
        
        // En C# el recolector de basura maneja la memoria
        Console.WriteLine("Elemento eliminado: " + elemento);
    }
    
    static void Mostrar() {
        if (front == null) {
            Console.WriteLine("La cola está vacía");
            return;
        }
        
        Console.WriteLine("Elementos de la cola:");
        Nodo actual = front;
        while (actual != null) {
            Console.WriteLine(actual.dato);
            actual = actual.siguiente;
        }
    }
    
    static void Main() {
        int opc = 0;
        
        while (opc != 4) {
            Console.WriteLine("\n*************** MENU QUEUE ***************");
            Console.WriteLine("1. Insertar elemento en la cola");
            Console.WriteLine("2. Eliminar elemento de la cola");
            Console.WriteLine("3. Mostrar la cola");
            Console.WriteLine("4. Salir");
            Console.Write("Ingrese su opción: ");
            
            if (!int.TryParse(Console.ReadLine(), out opc)) {
                opc = 0;
            }
            
            switch (opc) {
                case 1: Insertar(); break;
                case 2: Eliminar(); break;
                case 3: Mostrar(); break;
                case 4: Console.WriteLine("Saliendo del programa..."); break;
                default: Console.WriteLine("Opción inválida. Ingrese de nuevo"); break;
            }
        }
    }
}