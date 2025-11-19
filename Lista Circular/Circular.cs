using System;


public class Node
{
    public int Data;
    public Node Next;

    public Node(int data)
    {
        Data = data;
        Next = null;
    }
}

public class CircularLinkedList
{
    private Node last;

    public CircularLinkedList()
    {
        last = null;
    }

    

    public void InsertBegin()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Node newNode = new Node(value);

        if (last == null)
        {
            last = newNode;
            last.Next = last;
        }
        else
        {
            newNode.Next = last.Next;
            last.Next = newNode;
        }
    }

    public void InsertEnd()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Node newNode = new Node(value);
        if (last == null)
        {
            last = newNode;
            last.Next = last;
        }
        else
        {
            newNode.Next = last.Next;
            last.Next = newNode;
            last = newNode;
        }
    }

    public void InsertRandom()
    {
        Console.Write("Ingrese un valor: ");
        int value = int.Parse(Console.ReadLine());
        Console.Write("Ingrese la posicion donde desea insertar: ");
        int pos = int.Parse(Console.ReadLine());

        Node newNode = new Node(value);
        if (last == null)
        {
            if (pos <= 0)
            {
                last = newNode;
                last.Next = last;
            }
            return;
        }
        if (pos <= 0)
        {
            InsertBegin();
            return;
        }

        Node current = last.Next;
        for (int i = 0; i < pos - 1; i++)
        {
            if (current == last) break;
            current = current.Next;
        }
        newNode.Next = current.Next;
        current.Next = newNode;
        if (current == last)
        {
            last = newNode;
        }
    }

   

    public void DeleteBegin()
    {
        if (last == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Node temp = last.Next;
        if (last.Next == last)
        {
            last = null;
        }
        else
        {
            last.Next = temp.Next;
        }
    }

    public void DeleteEnd()
    {
        if (last == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        if (last.Next == last)
        {
            last = null;
            return;
        }
        Node temp = last.Next;
        while (temp.Next != last)
        {
            temp = temp.Next;
        }
        temp.Next = last.Next;
        last = temp;
        Console.WriteLine("Elemento eliminado desde el final");
    }

    public void DeleteRandom()
    {
        if (last == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Node current = last.Next;
        Node previous = last;
        Console.Write("Ingresa la posicion: ");
        int pos = int.Parse(Console.ReadLine());

        for (int i = 0; i < pos; i++)
        {
             if (current == last.Next && i > 0) { 
                Console.WriteLine("La posicion no existe");
                return;
            }
            previous = current;
            current = current.Next;
        }
        previous.Next = current.Next;
        if (current == last)
        {
            last = previous;
        }
        Console.WriteLine($"Elemento eliminado desde la posicion {pos}");
    }


   
    
    public void Search()
    {
        if (last == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Console.Write("Ingrese el valor a buscar: ");
        int value = int.Parse(Console.ReadLine());
        Node temp = last.Next;
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
        } while (temp != last.Next);
        Console.WriteLine($"Valor {value} no encontrado en la lista");
    }

    public void Display()
    {
        if (last == null)
        {
            Console.WriteLine("La lista esta vacia");
            return;
        }
        Node temp = last.Next;
        Console.Write("Lista Circular: ");
        do
        {
            Console.Write($"{temp.Data}-> ");
            temp = temp.Next;
        } while (temp != last.Next);
        Console.WriteLine("inicio");
    }
}

public class Program
{
    public static void Main()
    {
        CircularLinkedList cll = new CircularLinkedList();
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
                case 1: cll.InsertBegin(); break;
                case 2: cll.InsertEnd(); break;
                case 3: cll.InsertRandom(); break;
                case 4: cll.DeleteBegin(); break;
                case 5: cll.DeleteEnd(); break;
                case 6: cll.DeleteRandom(); break;
                case 7: cll.Search(); break;
                case 8: cll.Display(); break;
                case 9: Console.WriteLine("Saliendo..."); break;
                default: Console.WriteLine("Opcion invalida. Intente de nuevo.");
            }
        } while (choice != 9);
    }
}
