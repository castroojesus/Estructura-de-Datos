class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertbegin(self):
        value = int(input("Ingrese un valor: "))
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode

    def insertend(self):
        value = int(input("Ingrese un valor: "))
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            newNode.next = self.head
            newNode.prev = self.tail
            self.tail.next = newNode
            self.head.prev = newNode
            self.tail = newNode

    def insertrandom(self):
        value = int(input("Ingrese un valor: "))
        pos = int(input("Ingrese la posicion donde desea insertar: "))
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
        else:
            current = self.head
            for i in range(pos):
                current = current.next
                if current == self.head:
                    break
            newNode.next = current
            newNode.prev = current.prev
            current.prev.next = newNode
            current.prev = newNode
            if current == self.head and pos == 0:
                self.head = newNode
            if current == self.head:
                self.tail = newNode

    def deletebegin(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        print("Elemento eliminado desde el inicio")

    def deleteend(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        print("Elemento eliminado desde el final")

    def deleteRandom(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        current = self.head
        pos = int(input("Ingresa la posicion: "))
        for i in range(pos):
            current = current.next
            if current == self.head:
                print("La posicion no existe")
                return
        current.prev.next = current.next
        current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        if current == self.tail:
            self.tail = current.prev
        if self.head is None:
            self.tail = None
        print(f"Elemento eliminado desde la posicion {pos}")

    def search(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        value = int(input("Ingrese el valor a buscar: "))
        temp = self.head
        pos = 0
        while True:
            if temp.data == value:
                print(f"Valor {value} encontrado en la posicion {pos}")
                return
            temp = temp.next
            pos += 1
            if temp == self.head:
                break
        print(f"Valor {value} no encontrado en la lista")

    def display(self):
        if self.head is None:
            print("La lista esta vacia")
            return
        temp = self.head
        print("Lista Doble Circular: ", end="")
        while True:
            print(f"{temp.data} <-> ", end="")
            temp = temp.next
            if temp == self.head:
                break
        print("inicio")

if __name__ == "__main__":
    dcll = DoublyCircularLinkedList()
    while True:
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. insertar en posicion aleatoria")
        print("4. Eliminar al inicio")
        print("5. Eliminar al final")
        print("6. Eliminar desde posicion especifica")
        print("7. Buscar")
        print("8. Mostrar lista")
        print("9. Salir")
        choice = int(input("Ingrese su opcion: "))

        if choice == 1: dcll.insertbegin()
        elif choice == 2: dcll.insertend()
        elif choice == 3: dcll.insertrandom()
        elif choice == 4: dcll.deletebegin()
        elif choice == 5: dcll.deleteend()
        elif choice == 6: dcll.deleteRandom()
        elif choice == 7: dcll.search()
        elif choice == 8: dcll.display()
        elif choice == 9: break
        else: print("Opcion invalida. Intente de nuevo.")
