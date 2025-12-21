# PILA CON LISTA ENLAZADA
class Node:
    def __init__(self):
        self.data = 0        # dato del nodo
        self.next = None     # direccion al siguiente nodo

top = None    # puntero a tope de pila

# funcion para insertar en pila
def push(item):
    global top
    newNode = Node()        # crea un nodo
    newNode.data = item     # asigna el dato
    newNode.next = top      # el nuevo nodo apunta al anterior tope
    top = newNode           # el nuevo nodo es ahora el tope
    print(f"Elemento insertado: {item}")

# funcion para eliminar un elemento o extraer
def pop():
    global top
    if top is None:        # si la pila esta vacia
        print("STACK UNDERFLOW")
        return -1
    temp = top              # guarda el nodo del tope
    valor = top.data        # guarda el dato
    top = top.next          # mueve el tope al siguiente nodo
    del temp                # libera la memoria del nodo eliminado
    return valor

# funcion para ver el elemento superior 
def peek():
    if top is None:        # si esta vacia
        print("PILA VACIA")
        return -1
    return top.data        # retorna el valor del tope

# funcion para ver si la pila esta vacia
def is_empty():
    return top is None     # retorna True si el tope es None, o sea que esta vacia

def main():
    choice = 0
    while choice != 5:
        print("\n\n*********Menu Pila*********")
        print("1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Salir")
        try:
            choice = int(input("Ingrese su opción: "))
        except ValueError:
            choice = 0
        
        if choice == 1:
            try:
                valor = int(input("Ingrese el valor a insertar: "))
                push(valor)
            except ValueError:
                print("Entrada inválida")
        elif choice == 2:
            valor = pop()
            if valor != -1:
                print(f"Elemento extraído: {valor}")
        elif choice == 3:
            valor = peek()
            if valor != -1:
                print(f"Elemento superior: {valor}")
        elif choice == 4:
            print("La pila está vacía" if is_empty() else "La pila NO está vacía")
        elif choice == 5:
            print("Saliendo del programa...")
        else:
            print("Por favor, introduzca una opción válida")

if __name__ == "__main__":
    main()