class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insertbegin(self):
        value = int(input("Ingrese un valor: "))
        new_node = Node(value)
        
        if self.last is None:
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def insertend(self):
        value = int(input("Ingrese un valor: "))
        new_node = Node(value)
        if self.last is None:
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def insertrandom(self):
        value = int(input("Ingrese un valor: "))
        pos = int(input("Ingrese la posicion donde desea insertar: "))
        
        new_node = Node(value)
        if self.last is None:
            if pos <= 0:
                self.last = new_node
                self.last.next = self.last
            else:
                print("Posición inválida en lista vacía.")
                return

        current = self.last.next
        if pos <= 0:
            self.insert_begin()
            return
            
        for i in range(pos - 1):
            if current == self.last:
                break
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        
        if current == self.last:
            self.last = new_node

    def deletebegin(self):
        if self.last is None:
            print("La lista esta vacia")
            return
        temp = self.last.next
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = temp.next
        

    def deleteend(self):
        if self.last is None:
            print("La lista esta vacia")
            return
        if self.last.next == self.last:
            self.last = None
            return
        
        temp = self.last.next
        while temp.next != self.last:
            temp = temp.next
        temp.next = self.last.next
        self.last = temp
        print("Elemento eliminado desde el final")

    def deleterandom(self):
        if self.last is None:
            print("La lista esta vacia")
            return
        current = self.last.next
        previous = self.last
        pos = int(input("Ingresa la posicion: "))
        for i in range(pos):
            if current == self.last.next and i > 0: 
                 print("La posicion no existe")
                 return
            previous = current
            current = current.next
        previous.next = current.next
        if current == self.last:
            self.last = previous
        print(f"Elemento eliminado desde la posicion {pos}")

    def search(self):
        if self.last is None:
            print("La lista esta vacia")
            return
        value = int(input("Ingrese el valor a buscar: "))
        temp = self.last.next
        pos = 0
        while True:
            if temp.data == value:
                print(f"Valor {value} encontrado en la posicion {pos}")
                return
            temp = temp.next
            pos += 1
            if temp == self.last.next:
                break
        print(f"Valor {value} no encontrado en la lista")

    def display(self):
        if self.last is None:
            print("La lista esta vacia")
            return
        temp = self.last.next
        print("Lista Circular: ", end="")
        while True:
            print(f"{temp.data}-> ", end="")
            temp = temp.next
            if temp == self.last.next:
                break
        print("inicio")

def main():
    cll = CircularLinkedList()
    choice = 0
    while choice != 9:
        print("1. Agregar al inicio")
        print("2. Agregar al final")
        print("3. Agregar en posicion especifica")
        print("4. Eliminar desde el inicio")
        print("5. Eliminar desde el final")
        print("6. Eliminar desde posicion especifica")
        print("7. Mostrar lista")
        print("8. Buscar")
        print("9. Salir")

        try:
            opcion = input("Seleccione una opcion: ").strip()
            choice = int(opcion)
            match choice:
                case 1:
                    cll.insertbegin()

                case 2:
                    cll.insertend()
                case 3:
                    cll.insertrandom()
                case 4:
                    cll.deletebegin()
                case 5:
                    cll.deleteend()
                case 6:
                    cll.deleterandom()
                case 7:
                    cll.display()
                case 8:
                    cll.search()


        except ValueError:
            print("❌ Error: Por favor ingrese un número válido")
if __name__ == "__main__":
    main()
