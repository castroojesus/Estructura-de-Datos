import java.util.Scanner;

class Node {
    int data;
    Node next;
    Node prev;
}

public class DobleCircular {
    private Node head;
    private Node tail;
    private Scanner scanner = new Scanner(System.in);

    public DobleCircular() {
        this.head = null;
        this.tail = null;
    }

    public void insertbegin() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        Node newNode = new Node();
        newNode.data = value;
        if (head == null) {
            head = newNode;
            tail = newNode;
            newNode.next = newNode;
            newNode.prev = newNode;
        } else {
            newNode.next = head;
            newNode.prev = tail;
            head.prev = newNode;
            tail.next = newNode;
            head = newNode;
        }
    }

    public void insertend() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        Node newNode = new Node();
        newNode.data = value;
        if (head == null) {
            head = newNode;
            tail = newNode;
            newNode.next = newNode;
            newNode.prev = newNode;
        } else {
            newNode.next = head;
            newNode.prev = tail;
            tail.next = newNode;
            head.prev = newNode;
            tail = newNode;
        }
    }

    public void insertrandom() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        System.out.print("Ingrese la posicion donde desea insertar: ");
        int pos = scanner.nextInt();
        Node newNode = new Node();
        newNode.data = value;
        if (head == null) {
            head = newNode;
            tail = newNode;
            newNode.next = newNode;
            newNode.prev = newNode;
        } else {
            Node current = head;
            for (int i = 0; i < pos; i++) {
                current = current.next;
                if (current == head) {
                    break;
                }
            }
            newNode.next = current;
            newNode.prev = current.prev;
            current.prev.next = newNode;
            current.prev = newNode;
            if (current == head && pos == 0) {
                head = newNode;
            }
            if (current == head) {
                tail = newNode;
            }
        }
    }

    public void deletebegin() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        if (head == tail) {
            head = null;
            tail = null;
        } else {
            Node temp = head;
            head = head.next;
            head.prev = tail;
            tail.next = head;
        }
        System.out.println("Elemento eliminado desde el inicio");
    }

    public void deleteend() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        if (head == tail) {
            head = null;
            tail = null;
        } else {
            Node temp = tail;
            tail = tail.prev;
            tail.next = head;
            head.prev = tail;
        }
        System.out.println("Elemento eliminado desde el final");
    }

    public void deleteRandom() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        Node current = head;
        System.out.print("Ingresa la posicion: ");
        int pos = scanner.nextInt();
        for (int i = 0; i < pos; i++) {
            current = current.next;
            if (current == head) {
                System.out.println("La posicion no existe");
                return;
            }
        }
        current.prev.next = current.next;
        current.next.prev = current.prev;
        if (current == head) {
            head = current.next;
        }
        if (current == tail) {
            tail = current.prev;
        }
        if (head == null) {
            tail = null;
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
        do {
            if (temp.data == value) {
                System.out.println("Valor " + value + " encontrado en la posicion " + pos);
                return;
            }
            temp = temp.next;
            pos++;
        } while (temp != head);
        System.out.println("Valor " + value + " no encontrado en la lista");
    }

    public void display() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        Node temp = head;
        System.out.print("Lista Doble Circular: ");
        do {
            System.out.print(temp.data + " <-> ");
            temp = temp.next;
        } while (temp != head);
        System.out.println("inicio");
    }

    public static void main(String[] args) {
        DobleCircular dcll = new DobleCircular();
        int choice;
        do {
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
            choice = dcll.scanner.nextInt();

            switch (choice) {
                case 1: dcll.insertbegin(); break;
                case 2: dcll.insertend(); break;
                case 3: dcll.insertrandom(); break;
                case 4: dcll.deletebegin(); break;
                case 5: dcll.deleteend(); break;
                case 6: dcll.deleteRandom(); break;
                case 7: dcll.search(); break;
                case 8: dcll.display(); break;
                case 9: System.out.println("Saliendo..."); break;
                default: System.out.println("Opcion invalida. Intente de nuevo.");
            }
        } while (choice != 9);
        dcll.scanner.close();
    }
}

