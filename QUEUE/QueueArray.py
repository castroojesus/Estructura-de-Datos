# COLA CON ARRAYS
MAXSIZE = 5
queue = [0] * MAXSIZE
front = -1
rear = -1

def insertar():
    global front, rear
    elem = int(input("Ingrese el elemento: "))
    
    if rear == MAXSIZE - 1:
        print("OVERFLOW")
        return
    if front == -1 and rear == -1:
        front = rear = 0
    else:
        rear += 1
    queue[rear] = elem
    print("Elemento insertado correctamente")

def eliminar():
    global front, rear
    if front == -1 or front > rear:
        print("UNDERFLOW")
        return
    elemento = queue[front]
    if front == rear:
        front = rear = -1
    else:
        front += 1
    print(f"Elemento eliminado {elemento}")

def mostrar():
    if rear == -1 or front == -1 or front > rear:
        print("La cola esta vacia")
    else:
        print("Elementos de la cola: ")
        for i in range(front, rear + 1):
            print(queue[i])

def main():
    opc = 0
    
    while opc != 4:
        print("\n************************MENU QUEUE****************************")
        print("==================================================================")
        print("1. Insertar elemento en la cola")
        print("2. Eliminar elemento de la cola")
        print("3. Mostrar la cola")
        print("4. Salir")
        
        try:
            opc = int(input("Ingrese su opcion: "))
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
            print("\nOpcion invalida. Ingrese de nuevo\n")

if __name__ == "__main__":
    main()