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

def deletebegin():
    global head
    newNode = Nodo()
    if head is None:
        print("La lista esta vacia")
        return
    else:
        newNode = head
    head =newNode.next
    del newNode
    print("Nodo eliminado correctamente")

def deleteend():
    global head
    global temp
    newNode = Nodo()
    if head is None:
        print("La lista esta vacia")
        return
    else:
        newNode = head
        if newNode.next is None:
            head = None
            del newNode
            print("Nodo eliminado correctamente")
            return
        while newNode.next is not None:
            temp = newNode
            newNode = newNode.next
        temp.next = None
        del newNode
        print("Nodo eliminado correctamente")

def deleterandom():
    global head
    global temp
    newNode = Nodo()
    pos=input("Ingrese la posicion a agregar: ")
    newNode=head
    for i in range(int(pos)-1):
        if newNode is None:
            print("Error al agregar el nodo")
            return
        temp = newNode
        newNode = newNode.next
    temp.next=newNode.next
    del newNode
    print("El nodo eliminado correctamente")

def search():
    newNode = Nodo()
    global head
    pos =0
    if head is None:
        print("La lista esta vacia")
        return
    else:
        item = input("Ingrese el elemento a buscar: ")
        newNode=head
        while newNode is not None:
            if newNode.dato == item:
                print("El nodo se encuentra en la lista")
                flag = 0
                return
            else:
                flag = 1

            newNode = newNode.next
            pos=pos +1
            if flag==1:
                print("El nodo se encuentra en la lista")


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
                    insertbegin()

                case 2:
                    insertend()
                case 3:
                    randominsert()
                case 4:
                    deletebegin()
                case 5:
                    deleteend()
                case 6:
                    deleterandom()
                case 7:
                    display()
                case 8:
                    search()


        except ValueError:
            print("❌ Error: Por favor ingrese un número válido")
if __name__ == "__main__":
    main()