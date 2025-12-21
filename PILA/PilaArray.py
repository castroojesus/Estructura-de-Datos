# PILA
MAX_SIZE = 100
stack = [0] * MAX_SIZE      # arreglo de la pila
top = -1                    # elemento del tope de la pila

# funcion para insertar un elemento en la pila
def push(item):
    global top
    if top == MAX_SIZE - 1:   # si la pila está llena
        print("STACK OVERFLOW")
        return
    top += 1
    stack[top] = item         # incrementa el indice y agrega el elemento a la pila

# funcion para eliminar un elemento o sacar
def pop():
    global top
    if top == -1:             # si la pila esta vacia
        print("STACK UNDERFLOW")
        return -1
    valor = stack[top]
    top -= 1
    return valor

# funcion para ver el elemento superior sin eliminarlo
def peek():
    if top == -1:             # si esta vacia
        print("PILA VACIA")
        return -1
    return stack[top]         # retorna el valor del tope

# funcion para ver si la pila esta vacia
def is_empty():
    return top == -1          # retorna true si la pila es -1, o sea que esta vacia 

# funcion para ver si esta llena
def is_full():
    return top == MAX_SIZE - 1  # retorna true si esta llena, si el indice sup es igual al tamaño maximo menos uno

def main():
    choice = 0
    while choice != 6:
        print("\n\n*********Menu Pila*********")
        print("1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Verificar si está llena\n6. Salir")
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
            print("La pila está llena" if is_full() else "La pila NO está llena")
        elif choice == 6:
            print("Saliendo del programa...")
        else:
            print("Por favor, introduzca una opción válida")

if __name__ == "__main__":
    main()