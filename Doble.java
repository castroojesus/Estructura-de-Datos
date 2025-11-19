import java.util.Scanner;

class Node {
    int data;
    Node next;
    Node prev;

    public Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

public class Doble {
    private Node head;
    private Node tail;
    private Scanner scanner = new Scanner(System.in);

    public Doble() {
        this.head = null;
        this.tail = null;
    }

    

    public void insertbegin() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        Node newNode = new Node(value);
        newNode.next = head;
        newNode.prev = null;

        if (head != null) {
            head.prev = newNode;
        } else {
            tail = newNode;
        }
        head = newNode;
    }

    public void insertend() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        Node newNode = new Node(value);
        newNode.next = null;
        newNode.prev = tail;

        if (tail != null) {
            tail.next = newNode;
        } else {
            head = newNode;
        }
        tail = newNode;
    }

    public void insertrandom() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        System.out.print("Ingrese la posicion donde desea insertar: ");
        int pos = scanner.nextInt();

        if (pos <= 0 || head == null) {
            insertbegin();
            return;
        }

        Node current = head;
        for (int i = 0; i < pos - 1; i++) {
            if (current.next == null) {
                insertend();
                return;
            }
            current = current.next;
        }

        Node newNode = new Node(value);
        newNode.next = current.next;
        newNode.prev = current;

        if (current.next != null) {
            current.next.prev = newNode;
        } else {
            tail = newNode;
        }
        current.next = newNode;
        System.out.println("Elemento insertado en la posicion " + pos);
    }

    

    public void deletebegin() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        Node temp = head;
        head = head.next;
        if (head != null) {
            head.prev = null;
        } else {
            tail = null;
        }
        
        System.out.println("Elemento eliminado desde el inicio");
    }

    public void deleteend() {
        if (tail == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        Node temp = tail;
        tail = tail.prev;
        if (tail != null) {
            tail.next = null;
        } else {
            head = null;
        }
        
        System.out.println("Elemento eliminado desde el final");
    }
    
    public void deleteRandom() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        System.out.print("Ingresa la posicion: ");
        int pos = scanner.nextInt();

        Node current = head;
        for (int i = 0; i < pos; i++) {
            if (current == null) {
                System.out.println("La posicion no existe");
                return;
            }
            current = current.next;
        }

        if (current.prev != null) {
            current.prev.next = current.next;
        } else {
            head = current.next;
        }

        if (current.next != null) {
            current.next.prev = current.prev;
        } else {
            tail = current.prev;
        }
        
        System.out.println("Elemento eliminado desde la posicion " + pos);
    }

    

    public void search() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        System.out.print("Ingrese el valor a buscar: ");
        int value = scanner.nextInt();
        Node temp = head;
        int pos = 0;
        while (temp != null) {
            if (temp.data == value) {
                System.out.println("Valor " + value + " encontrado en la posicion " + pos);
                return;
            }
            temp = temp.next;
            pos++;
        }
        System.out.println("Valor " + value + " no encontrado en la lista");
    }

    public void display() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        Node temp = head;
        System.out.print("Lista Doble: ");
        while (temp != null) {
            System.out.print(temp.data + " <-> ");
            temp = temp.next;
        }
        System.out.println("NULL");
    }

    
    public static void main(String[] args) {
        Doble dll = new Doble();
        int choice;

        do {
            System.out.println("\n----------------------------------");
            System.out.println("1. Insertar al inicio");
            System.out.println("2. Insertar al final");
            System.out.println("3. insertar en posicion aleatoria");
            System.out.println("4. Eliminar al inicio");
            System.out.println("5. Eliminar al final");
            System.out.println("6. Eliminar desde posicion especifica");
            System.out.println("7. Buscar");
            System.out.println("8. Mostrar lista");
            System.out.println("9. Salir");
            System.out.print("Ingrese su opcion: ");
            choice = dll.scanner.nextInt();

            switch (choice) {
                case 1: dll.insertbegin(); break;
                case 2: dll.insertend(); break;
                case 3: dll.insertrandom(); break;
                case 4: dll.deletebegin(); break;
                case 5: dll.deleteend(); break;
                case 6: dll.deleteRandom(); break;
                case 7: dll.search(); break;
                case 8: dll.display(); break;
                case 9: System.out.println("Saliendo..."); break;
                default: System.out.println("Opcion invalida. Intente de nuevo.");
            }
        } while (choice != 9);
        dll.scanner.close();
    }
}
