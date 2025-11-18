using System;

class Node {
    public int data;
    public Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    static Node head;
    
    static void Main() {
        int choice = 0;
        while (choice != 9) {
            Console.WriteLine("\n*********Main Menu*********");
            Console.WriteLine("1. Agregar al inicio");
            Console.WriteLine("2. Agregar al final");
            Console.WriteLine("3. Agregar en una posicion aleatoria");
            Console.WriteLine("4. Eliminar desde el inicio");
            Console.WriteLine("5. Eliminar desde el final");
            Console.WriteLine("6. Eliminar desde una posicion aleatoria");
            Console.WriteLine("7. Mostrar");
            Console.WriteLine("8. Buscar");
            Console.WriteLine("9. Salir");
            Console.Write("Ingresa tu opciom: ");
            choice = Convert.ToInt32(Console.ReadLine());
            
            switch (choice) {
                case 1:
                    InsertBeg();
                    break;
                case 2:
                    InsertEnd();
                    break;
                case 3:
                    RandomInsert();
                    break;
                case 4:
                    DeleteBeg();
                    break;
                case 5:
                    DeleteEnd();
                    break;
                case 6:
                    RandomDelete();
                    break;
                case 7:
                    Display();
                    break;
                case 8:
                    Search();
                    break;
                case 9:
                    Environment.Exit(0);
                    break;
                default:
                    Console.WriteLine("Opcion invalida! Por favor intenta de nuevo.");
                    break;
            }
        }
    }
    
    static void InsertBeg() {
        Console.Write("Ingresa un elemento: ");
        int item = Convert.ToInt32(Console.ReadLine());
        Node newNode = new Node(item);
        newNode.next = head;
        head = newNode;
        Console.WriteLine("Elemento insertado");
    }
    
    static void InsertEnd() {
        Console.Write("Ingresa un elemento: ");
        int item = Convert.ToInt32(Console.ReadLine());
        Node newNode = new Node(item);
        
        if (head == null) {
            head = newNode;
            Console.WriteLine("Elemento insertado");
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
            Console.WriteLine("Elemento insertado");
        }
    }
    
    static void RandomInsert() {
        Console.Write("Ingresa un elemento: ");
        int item = Convert.ToInt32(Console.ReadLine());
        Console.Write("Ingresa la posicion: ");
        int pos = Convert.ToInt32(Console.ReadLine());
        
        Node newNode = new Node(item);
        Node temp = head;
        
        for (int i = 0; i < pos - 1; i++) {
            if (temp == null) {
                Console.WriteLine("La posicion no existe");
                return;
            }
            temp = temp.next;
        }
        
        if (temp != null) {
            newNode.next = temp.next;
            temp.next = newNode;
            Console.WriteLine("Elemento insertado");
        } else {
            Console.WriteLine("La posicion no existe");
        }
    }
    
    static void DeleteBeg() {
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else {
            head = head.next;
            Console.WriteLine("Elemento eliminado desde el principio");
        }
    }
    
    static void DeleteEnd() {
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else if (head.next == null) {
            head = null;
            Console.WriteLine("Solo se elimino un nodo de la lista");
        } else {
            Node temp = head;
            Node prev = null;
            while (temp.next != null) {
                prev = temp;
                temp = temp.next;
            }
            prev.next = null;
            Console.WriteLine("Elemento eliminado desde el final");
        }
    }
    
    static void RandomDelete() {
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        
        Console.Write("Ingresa la posicion: ");
        int pos = Convert.ToInt32(Console.ReadLine());
        
        if (pos == 0) {
            DeleteBeg();
            return;
        }
        
        Node temp = head;
        Node prev = null;
        
        for (int i = 0; i < pos; i++) {
            if (temp == null) {
                Console.WriteLine("La posicion no existe");
                return;
            }
            prev = temp;
            temp = temp.next;
        }
        
        if (temp != null) {
            prev.next = temp.next;
            Console.WriteLine("Elemento eliminado desde la posicion " + (pos + 1));
        } else {
            Console.WriteLine("La posicion no existe");
        }
    }
    
    static void Display() {
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
        } else {
            Console.Write("Elementos en la lista: ");
            Node temp = head;
            while (temp != null) {
                Console.Write(temp.data + " ");
                temp = temp.next;
            }
            Console.WriteLine();
        }
    }
    
    static void Search() {
        if (head == null) {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        
        Console.Write("Ingresa el elemento a buscar: ");
        int item = Convert.ToInt32(Console.ReadLine());
        
        Node temp = head;
        int pos = 0;
        bool found = false;
        
        while (temp != null) {
            if (temp.data == item) {
                Console.WriteLine("Elemento " + item + " encontrado en la posicion " + pos);
                found = true;
            }
            temp = temp.next;
            pos++;
        }
        
        if (!found) {
            Console.WriteLine("Elemento no encontrado en la lista");
        }
    }
}