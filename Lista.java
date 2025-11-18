import java.util.Scanner;

class Node {
    int data;
    Node next;
    
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Lista {
    static Node head;
    static Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        int choice = 0;
        while (choice != 9) {
            System.out.println("\n*********Main Menu*********");
            System.out.println("1. Agergar al inicio");
            System.out.println("2. Agregar al final");
            System.out.println("3. Agregar en una posicion aleatoria");
            System.out.println("4. Eliminar desde el inicio");
            System.out.println("5. Eliminar desde el final");
            System.out.println("6. Eliminar desde una posicion aleatoria");
            System.out.println("7. Mostrar");
            System.out.println("8. Buscar");
            System.out.println("9. Salir");
            System.out.print("Ingresa tu opcion: ");
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    insertbeg();
                    break;
                case 2:
                    insertend();
                    break;
                case 3:
                    randominsert();
                    break;
                case 4:
                    deletebeg();
                    break;
                case 5:
                    deleteend();
                    break;
                case 6:
                    randomdelete();
                    break;
                case 7:
                    display();
                    break;
                case 8:
                    search();
                    break;
                case 9:
                    System.exit(0);
                default:
                    System.out.println("Opcion invalida! Por favor intenta de nuevo.");
            }
        }
    }
    
    static void insertbeg() {
        System.out.print("Ingresa un elemento: ");
        int item = scanner.nextInt();
        Node newNode = new Node(item);
        newNode.next = head;
        head = newNode;
        System.out.println("Elemento insertado");
    }
    
    static void insertend() {
        System.out.print("Ingresa un elemento: ");
        int item = scanner.nextInt();
        Node newNode = new Node(item);
        
        if (head == null) {
            head = newNode;
            System.out.println("Elemento insertado");
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
            System.out.println("Elemento insertado");
        }
    }
    
    static void randominsert() {
        System.out.print("Ingresa un elemento: ");
        int item = scanner.nextInt();
        System.out.print("Ingresa la posicion: ");
        int pos = scanner.nextInt();
        
        Node newNode = new Node(item);
        Node temp = head;
        
        for (int i = 0; i < pos - 1; i++) {
            if (temp == null) {
                System.out.println("La posicion no existe");
                return;
            }
            temp = temp.next;
        }
        
        if (temp != null) {
            newNode.next = temp.next;
            temp.next = newNode;
            System.out.println("Elemento insertado");
        } else {
            System.out.println("La posicion no existe");
        }
    }
    
    static void deletebeg() {
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else {
            Node temp = head;
            head = head.next;
            temp = null;
            System.out.println("Elemento eliminado desde el principio");
        }
    }
    
    static void deleteend() {
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else if (head.next == null) {
            head = null;
            System.out.println("Solo se elimino un nodo de la lista");
        } else {
            Node temp = head;
            Node prev = null;
            while (temp.next != null) {
                prev = temp;
                temp = temp.next;
            }
            prev.next = null;
            temp = null;
            System.out.println("Elemento eliminado desde el final");
        }
    }
    
    static void randomdelete() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        
        System.out.print("Ingresa la posicion: ");
        int pos = scanner.nextInt();
        
        if (pos == 0) {
            deletebeg();
            return;
        }
        
        Node temp = head;
        Node prev = null;
        
        for (int i = 0; i < pos; i++) {
            if (temp == null) {
                System.out.println("La posicion no existe");
                return;
            }
            prev = temp;
            temp = temp.next;
        }
        
        if (temp != null) {
            prev.next = temp.next;
            temp = null;
            System.out.println("Elemento eliminado desde la posicion " + (pos + 1));
        } else {
            System.out.println("La posicion no existe");
        }
    }
    
    static void display() {
        if (head == null) {
            System.out.println("La lista esta vacia");
        } else {
            System.out.print("Elementos en la lista: ");
            Node temp = head;
            while (temp != null) {
                System.out.print(temp.data + " ");
                temp = temp.next;
            }
            System.out.println();
        }
    }
    
    static void search() {
        if (head == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        
        System.out.print("Ingresa el elemento a buscar: ");
        int item = scanner.nextInt();
        
        Node temp = head;
        int pos = 0;
        boolean found = false;
        
        while (temp != null) {
            if (temp.data == item) {
                System.out.println("Elemento " + item + " encontrado en la posicion " + pos);
                found = true;
            }
            temp = temp.next;
            pos++;
        }
        
        if (!found) {
            System.out.println("Elemento no encontrado en la lista");
        }
    }
}
