using System;

public class Node
{
    public int Data;
    public Node Next;
    public Node Prev;

    public Node(int data)
    {
        Data = data;
        Next = null;
        Prev = null;
    }
}

public class DoublyLinkedList
{
    private Node head;
    private Node tail;

    public DoublyLinkedList()
    {
        head = null;
        tail = null;
    }

    

    public void InsertBegin()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Node newNode = new Node(value);
        newNode.Next = head;
        newNode.Prev = null;

        if (head != null)
        {
            head.Prev = newNode;
        }
        else
        {
            tail = newNode;
        }
        head = newNode;
    }

    public void InsertEnd()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Node newNode = new Node(value);
        newNode.Next = null;
        newNode.Prev = tail;

        if (tail != null)
        {
            tail.Next = newNode;
        }
        else
        {
            head = newNode;
        }
        tail = newNode;
    }

    public void InsertRandom()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Console.Write("Ingrese la posicion donde desea insertar: ");
        int pos = int.Parse(Console.ReadLine());

        if (pos <= 0 || head == null)
        {
            InsertBegin();
            return;
        }

        Node current = head;
        for (int i = 0; i < pos - 1; i++)
        {
            if (current.Next == null)
            {
                InsertEnd();
                return;
            }
            current = current.Next;
        }

        Node newNode = new Node(value);
        newNode.Next = current.Next;
        newNode.Prev = current;

        if (current.Next != null)
        {
            current.Next.Prev = newNode;
        }
        else
        {
            tail = newNode;
        }
        current.Next = newNode;
        Console.WriteLine($"Elemento insertado en la posicion {pos}");
    }

   

    public void DeleteBegin()
    {
        if (head == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Node temp = head;
        head = head.Next;
        if (head != null)
        {
            head.Prev = null;
        }
        else
        {
            tail = null;
        }
        Console.WriteLine("Elemento eliminado desde el inicio");
    }

    public void DeleteEnd()
    {
        if (tail == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Node temp = tail;
        tail = tail.Prev;
        if (tail != null)
        {
            tail.Next = null;
        }
        else
        {
            head = null;
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
        Console.Write("Ingresa la posicion: ");
        int pos = int.Parse(Console.ReadLine());

        Node current = head;
        for (int i = 0; i < pos; i++)
        {
            if (current == null)
            {
                Console.WriteLine("La posicion no existe");
                return;
            }
            current = current.Next;
        }

        if (current.Prev != null)
        {
            current.Prev.Next = current.Next;
        }
        else
        {
            head = current.Next;
        }

        if (current.Next != null)
        {
            current.Next.Prev = current.Prev;
        }
        else
        {
            tail = current.Prev;
        }
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
        while (temp != null)
        {
            if (temp.Data == value)
            {
                Console.WriteLine($"Valor {value} encontrado en la posicion {pos}");
                return;
            }
            temp = temp.Next;
            pos++;
        }
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
        Console.Write("Lista Doble: ");
        while (temp != null)
        {
            Console.Write($"{temp.Data} <-> ");
            temp = temp.Next;
        }
        Console.WriteLine("NULL");
    }
}


public class Program
{
    public static void Main()
    {
        DoublyLinkedList dll = new DoublyLinkedList();
        int choice;

        do
        {
            Console.WriteLine("\n----------------------------------");
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
                case 1: dll.InsertBegin(); break;
                case 2: dll.InsertEnd(); break;
                case 3: dll.InsertRandom(); break;
                case 4: dll.DeleteBegin(); break;
                case 5: dll.DeleteEnd(); break;
                case 6: dll.DeleteRandom(); break;
                case 7: dll.Search(); break;
                case 8: dll.Display(); break;
                case 9: Console.WriteLine("Saliendo..."); break;
                default: Console.WriteLine("Opcion invalida. Intente de nuevo.");
            }
        } while (choice != 9);
    }
}
