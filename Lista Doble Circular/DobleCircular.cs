using System;

public class Node
{
    public int Data;
    public Node Next;
    public Node Prev;
}

public class DoublyCircularLinkedList
{
    private Node head;
    private Node tail;

    public DoublyCircularLinkedList()
    {
        head = null;
        tail = null;
    }

    public void InsertBegin()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Node newNode = new Node();
        newNode.Data = value;

        if (head == null)
        {
            head = newNode;
            tail = newNode;
            newNode.Next = newNode;
            newNode.Prev = newNode;
        }
        else
        {
            newNode.Next = head;
            newNode.Prev = tail;
            head.Prev = newNode;
            tail.Next = newNode;
            head = newNode;
        }
    }

    public void InsertEnd()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Node newNode = new Node();
        newNode.Data = value;

        if (head == null)
        {
            head = newNode;
            tail = newNode;
            newNode.Next = newNode;
            newNode.Prev = newNode;
        }
        else
        {
            newNode.Next = head;
            newNode.Prev = tail;
            tail.Next = newNode;
            head.Prev = newNode;
            tail = newNode;
        }
    }

    public void InsertRandom()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Console.Write("Ingrese la posicion donde desea insertar: ");
        int pos = int.Parse(Console.ReadLine());

        Node newNode = new Node();
        newNode.Data = value;

        if (head == null)
        {
            head = newNode;
            tail = newNode;
            newNode.Next = newNode;
            newNode.Prev = newNode;
        }
        else
        {
            Node current = head;
            for (int i = 0; i < pos; i++)
            {
                current = current.Next;
                if (current == head) break;
            }
            newNode.Next = current;
            newNode.Prev = current.Prev;
            current.Prev.Next = newNode;
            current.Prev = newNode;

            if (current == head && pos == 0) head = newNode;
            if (current == head) tail = newNode;
        }
    }

    public void DeleteBegin()
    {
        if (head == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        if (head == tail)
        {
            head = null;
            tail = null;
        }
        else
        {
            Node temp = head;
            head = head.Next;
            head.Prev = tail;
            tail.Next = head;
        }
        Console.WriteLine("Elemento eliminado desde el inicio");
    }

    public void DeleteEnd()
    {
        if (head == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        if (head == tail)
        {
            head = null;
            tail = null;
        }
        else
        {
            Node temp = tail;
            tail = tail.Prev;
            tail.Next = head;
            head.Prev = tail;
        }
        Console.WriteLine("Elemento eliminado desde el final");
    }

    public void DeleteRandom()
    {
        if (head == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Node current = head;
        Console.Write("Ingresa la posicion: ");
        int pos = int.Parse(Console.ReadLine());
        for (int i = 0; i < pos; i++)
        {
            current = current.Next;
            if (current == head)
            {
                Console.WriteLine("La posicion no existe");
                return;
            }
        }
        current.Prev.Next = current.Next;
        current.Next.Prev = current.Prev;

        if (current == head) head = current.Next;
        if (current == tail) tail = current.Prev;
        if (head == null) tail = null;
        Console.WriteLine($"Elemento eliminado desde la posicion {pos}");
    }

    public void Search()
    {
        if (head == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Console.Write("Ingrese el valor a buscar: ");
        int value = int.Parse(Console.ReadLine());
        Node temp = head;
        int pos = 0;
        do
        {
            if (temp.Data == value)
            {
                Console.WriteLine($"Valor {value} encontrado en la posicion {pos}");
                return;
            }
            temp = temp.Next;
            pos++;
        } while (temp != head);
        Console.WriteLine($"Valor {value} no encontrado en la lista");
    }

    public void Display()
    {
        if (head == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Node temp = head;
        Console.Write("Lista Doble Circular: ");
        do
        {
            Console.Write($"{temp.Data} <-> ");
            temp = temp.Next;
        } while (temp != head);
        Console.WriteLine("inicio");
    }
}

public class Program
{
    public static void Main()
    {
        DoublyCircularLinkedList dcll = new DoublyCircularLinkedList();
        int choice;
        do
        {
            Console.WriteLine("1. Insertar al inicio");
            Console.WriteLine("2. Insertar al final");
            Console.WriteLine("3. insertar en posicion aleatoria");
            Console.WriteLine("4. Eliminar al inicio");
            Console.WriteLine("5. Eliminar al final");
            Console.WriteLine("6. Eliminar desde posicion especifica");
            Console.WriteLine("7. Buscar");
            Console.WriteLine("8. Mostrar lista");
            Console.WriteLine("9. Salir");
            Console.Write("Ingrese su opcion: ");
            choice = int.Parse(Console.ReadLine());

            switch (choice)
            {
                case 1: dcll.InsertBegin(); break;
                case 2: dcll.InsertEnd(); break;
                case 3: dcll.InsertRandom(); break;
                case 4: dcll.DeleteBegin(); break;
                case 5: dcll.DeleteEnd(); break;
                case 6: dcll.DeleteRandom(); break;
                case 7: dcll.Search(); break;
                case 8: dcll.Display(); break;
                case 9: Console.WriteLine("Saliendo..."); break;
                default: Console.WriteLine("Opcion invalida. Intente de nuevo.");
            }
        } while (choice != 9);
    }
}
