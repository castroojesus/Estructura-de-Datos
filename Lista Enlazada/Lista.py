


class Nodo:
    def __init__(self):
        self.dato = None
        self.next = None


head = None
temp = None


def insertbegin():
    global head
    newNode = Nodo()
    if newNode is None:
        print("Error al crear el nodo")
        return
    else:
        dato = input("Ingrese el dato a agregar al inicio: ")
        newNode.dato = dato
        newNode.next = head
        head = newNode

def insertend():
    global head
    global temp
    newNode = Nodo()
    if newNode is None:
        print("Error al crear el nodo")
    else:
        item = input("Ingrese el dato a agregar al final: ")
        newNode.dato = item
        if head is None:
            newNode.next = None
            head = newNode
            print("El nodo ha sido creado correctamente")
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            newNode.next = None
            print("El nodo ha sido actualizado correctamente")

def randominsert():
    global head
    global temp
    newNode = Nodo()
    if newNode is None:
        print("Error al crear el nodo")
    else:
        item = input("Ingrese el dato a agregar: ")
        newNode.dato = item
        pos= input("Ingrese la posicion a agregar: ")
        temp = head
        i=0
        for i in range(int(pos)-1):
            if temp is None:
                print("Error al agregar el nodo")
                return
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        print("El nodo ha sido actualizado correctamente")

def display():

    newNode = Nodo()
    newNode = head
    if newNode is None:
        print("La lista esta vacia")
    else:
        print("Elementos de la lista:")
        while newNode is not None:
            print(newNode.dato + " -> ")
            newNode = newNode.next
        print("\n")

def main():
    choice = 0
    while choice != 9:
        print("1. Agregar al inicio")
        print("2. Agregar al final")
        print("3. Eliminar un nodo")
        print("4. Buscar un nodo")
        print("5. Mostrar lista")
        print("6. Contar nodos")
        print("7. Invertir lista")
        print("8. Buscar")
        print("9. Salir")

        try:
            opcion = input("Seleccione una opcion: ").strip()
            choice = int(opcion)
            match choice:
                case 1:
                    insertbegin()

                case 2:
                    insertend()
                case 3:
                    randominsert()
                case 4:
                    display()
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido")
if __name__ == "__main__":
    main()