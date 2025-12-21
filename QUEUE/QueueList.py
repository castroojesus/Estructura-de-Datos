# Estructura del nodo
class Nodo:
    def __init__(self):
        self.dato = 0
        self.siguiente = None

front = None
rear = None

def insertar():
    global front, rear
    elem = int(input("Ingrese el elemento: "))
    
    nuevo = Nodo()
    nuevo.dato = elem
    nuevo.siguiente = None
    
    if front is None and rear is None:
        front = rear = nuevo
    else:
        rear.siguiente = nuevo
        rear = nuevo
    
    print("Elemento insertado correctamente")

def eliminar():
    global front, rear
    if front is None:
        print("UNDERFLOW")
        return
    
    temp = front
    elemento = temp.dato
    
    front = front.siguiente
    if front is None:
        rear = None
    
    del temp  # Libera la memoria
    print(f"Elemento eliminado: {elemento}")

def mostrar():
    if front is None:
        print("La cola está vacía")
        return
    
    print("Elementos de la cola:")
    actual = front
    while actual is not None:
        print(actual.dato)
        actual = actual.siguiente

def main():
    opc = 0
    
    while opc != 4:
        print("\n*************** MENU QUEUE ***************")
        print("1. Insertar elemento en la cola")
        print("2. Eliminar elemento de la cola")
        print("3. Mostrar la cola")
        print("4. Salir")
        
        try:
            opc = int(input("Ingrese su opción: "))
        except ValueError:
            opc = 0
        
        if opc == 1:
            insertar()
        elif opc == 2:
            eliminar()
        elif opc == 3:
            mostrar()
        elif opc == 4:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Ingrese de nuevo")

if __name__ == "__main__":
    main()