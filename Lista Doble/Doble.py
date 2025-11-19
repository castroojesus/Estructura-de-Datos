class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertbegin(self):
        value = int(input("Ingrese un valor: "))
        newNode = Node(value)
        newNode.next = self.head
        newNode.prev = None

        if self.head is not None:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode

    def insertend(self):
        value = int(input("Ingrese un valor: "))
        newNode = Node(value)
        newNode.next = None
        newNode.prev = self.tail

        if self.tail is not None:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode

    def insertrandom(self):
        value = int(input("Ingrese un valor: "))
        pos = int(input("Ingrese la posicion donde desea insertar: "))

        if pos <= 0 or self.head is None:
            self.insertbegin()
            return

        current = self.head
        for i in range(pos - 1):
            if current.next is None:
                self.insertend()
                return
            current = current.next
        
        newNode = Node(value)
        newNode.next = current.next
        newNode.prev = current

        if current.next is not None:
            current.next.prev = newNode
        else:
            self.tail = newNode
        current.next = newNode
        print(f"Elemento insertado en la posicion {pos}")

    def deletebegin(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        
        print("Elemento eliminado desde el inicio")

    def deleteend(self):
        if self.tail is None:
            print("La lista esta vacia")
            return
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        
        print("Elemento eliminado desde el final")

    def deleteRandom(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        pos = int(input("Ingresa la posicion: "))
        current = self.head
        
        for i in range(pos):
            if current is None:
                print("La posicion no existe")
                return
            current = current.next

        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        
       
        print(f"Elemento eliminado desde la posicion {pos}")

    def search(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        value = int(input("Ingrese el valor a buscar: "))
        temp = self.head
        pos = 0
        while temp is not None:
            if temp.data == value:
                print(f"Valor {value} encontrado en la posicion {pos}")
                return
            temp = temp.next
            pos += 1
        print(f"Valor {value} no encontrado en la lista")

    def display(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        temp = self.head
        print("Lista Doble: ", end="")
        while temp is not None:
            print(f"{temp.data} <-> ", end="")
            temp = temp.next
        print("NULL")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    while True:
        print("\n1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. insertar en posicion aleatoria")
        print("4. Eliminar al inicio")
        print("5. Eliminar al final")
        print("6. Eliminar desde posicion especifica")
        print("7. Buscar")
        print("8. Mostrar lista")
        print("9. Salir")
        choice = int(input("Ingrese su opcion: "))

        if choice == 1: dll.insertbegin()
        elif choice == 2: dll.insertend()
        elif choice == 3: dll.insertrandom()
        elif choice == 4: dll.deletebegin()
        elif choice == 5: dll.deleteend()
        elif choice == 6: dll.deleteRandom()
        elif choice == 7: dll.search()
        elif choice == 8: dll.display()
        elif choice == 9: 
            print("Saliendo...")
            break
        else: print("Opcion invalida. Intente de nuevo.")
