import java.util.Scanner;


class Node {
    int data;
    Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}


public class Circular {
    private Node last;
    private Scanner scanner = new Scanner(System.in);

    public Circular() {
        this.last = null;
    }

    
    public void insertBegin() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        Node newNode = new Node(value);
        
        if (last == null) {
            last = newNode;
            last.next = last;
        } else {
            newNode.next = last.next;
            last.next = newNode;
        }
    }
    
    public void insertEnd() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        Node newNode = new Node(value);
        if (last == null) {
            last = newNode;
            last.next = last;
        } else {
            newNode.next = last.next;
            last.next = newNode;
            last = newNode;
        }
    }
    
    public void insertRandom() {
        System.out.print("Ingrese un valor: ");
        int value = scanner.nextInt();
        System.out.print("Ingrese la posicion donde desea insertar: ");
        int pos = scanner.nextInt();

        Node newNode = new Node(value);
        if (last == null) {
            if (pos <= 0) {
                last = newNode;
                last.next = last;
            }
            return;
        }
        if (pos <= 0) {
            insertBegin();
            return;
        }

        Node current = last.next;
        for (int i = 0; i < pos - 1; i++) {
            if (current == last) {
                break;
            }
            current = current.next;
        }
        newNode.next = current.next;
        current.next = newNode;
        if (current == last) {
            last = newNode;
        }
    }

    

    public void deleteBegin() {
        if (last == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        Node temp = last.next;
        if (last.next == last) { 
            last = null;
        } else {
            last.next = temp.next;
        }
        
    }

    public void deleteEnd() {
        if (last == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        if (last.next == last) { 
            last = null;
            return;
        }
        Node temp = last.next;
        while (temp.next != last) {
            temp = temp.next;
        }
        temp.next = last.next;
        last = temp;
        System.out.println("Elemento eliminado desde el final");
    }

    public void deleteRandom() {
        if (last == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        Node current = last.next;
        Node previous = last;
        System.out.print("Ingresa la posicion: ");
        int pos = scanner.nextInt();

        for (int i = 0; i < pos; i++) {
            
             if (current == last && i >= pos -1) { 
                System.out.println("La posicion no existe");
                return;
            }
            previous = current;
            current = current.next;
        }
        previous.next = current.next;
        if (current == last) {
            last = previous;
        }
        System.out.println("Elemento eliminado desde la posicion " + pos);
    }

   

    public void search() {
        if (last == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        System.out.print("Ingrese el valor a buscar: ");
        int value = scanner.nextInt();
        Node temp = last.next;
        int pos = 0;
        do {
            if (temp.data == value) {
                System.out.println("Valor " + value + " encontrado en la posicion " + pos);
                return;
            }
            temp = temp.next;
            pos++;
        } while (temp != last.next);
        System.out.println("Valor " + value + " no encontrado en la lista");
    }

    public void display() {
        if (last == null) {
            System.out.println("La lista esta vacia");
            return;
        }
        Node temp = last.next;
        System.out.print("Lista Circular: ");
        do {
            System.out.print(temp.data + "-> ");
            temp = temp.next;
        } while (temp != last.next);
        System.out.println("inicio");
    }

    
    public static void main(String[] args) {
        Circular cll = new Circular();
        Scanner scanner = new Scanner(System.in);
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
            choice = scanner.nextInt();

            switch (choice) {
                case 1: cll.insertBegin(); break;
                case 2: cll.insertEnd(); break;
                case 3: cll.insertRandom(); break;
                case 4: cll.deleteBegin(); break;
                case 5: cll.deleteEnd(); break;
                case 6: cll.deleteRandom(); break;
                case 7: cll.search(); break;
                case 8: cll.display(); break;
                case 9: System.out.println("Saliendo..."); break;
                default: System.out.println("Opcion invalida. Intente de nuevo.");
            }
        } while (choice != 9);
        scanner.close();
    }
}
