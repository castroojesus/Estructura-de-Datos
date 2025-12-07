from unittest import case

from Node import Node

class Arbol():
    #raiz
    def __init__(self):
        self.root = None
    #metodo de insercion
    def insert(self,valor):
        self.root= self.insertrec(self.root,valor)

    def insertrec(self,current,valor):
        #si el arbol esta vacio se agrega el nuevo valor
        if current is None:
            return Node(valor)
        #si el valor es menor al que ya existe entonces se recorre al subarbol izquierdo
        if valor < current.valor:
            current.left = self.insertrec(current.left,valor)
        elif valor > current.valor:
        #si es mayor al derecho
            current.right = self.insertrec(current.right,valor)
        return current
    def delete(self,valor):
        self.root = self.deleterec(self.root,valor)
    def deleterec(self,current,valor):
        if current is None:
            return None
        if valor < current.valor:
            current.left = self.deleterec(current.left,valor)
        elif valor > current.valor:
            current.right = self.deleterec(current.right,valor)
        else:
            if current.left is None and current.right is None:
                return None
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            sucesor = self.findsucessor(current.right)
            current.valor = sucesor.valor
            current.right=self.deleterec(current.right,sucesor.valor)
        return current
    def findsucessor(self,nodo):
        while nodo.left:
            nodo = nodo.left
        return nodo
    def inorder(self):
        self.inorderrec(self.root)
        print()
    def inorderrec(self,nodo):
        if nodo:
            self.inorderrec(nodo.left)
            print(nodo.valor, end=' ')
            self.inorderrec(nodo.right)
    def preorder(self):
        self.preorderrec(self.root)
        print()

    def preorderrec(self,nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.preorderrec(nodo.left)
            self.preorderrec(nodo.right)

    def postorder(self):
        self.postorderrec(self.root)
        print()

    def postorderrec(self,nodo):
        if nodo:
            self.postorderrec(nodo.left)
            self.postorderrec(nodo.right)
            print(nodo.valor, end=' ')
    def search(self,valor):

        resultado =(self.searchrec(self.root,valor))
        if resultado:
            print(f" Valor {valor} encontrado en el árbol")
        else:
            print(f" Valor {valor} NO encontrado en el árbol")
        return resultado

    def searchrec(self,current,valor):
        if current is None:
            return None

        if valor == current.valor:
            return current

        if valor < current.valor:
            return self.searchrec(current.left,valor)
        elif valor > current.valor:
            return self.searchrec(current.right,valor)

    def height(self):
       return self.heightrec(self.root)
    def heightrec(self,current):
        if current is None:
            return 0
        return 1 + max(self.heightrec(current.left), self.heightrec(current.right))

    def size(self):
        return self.sizerec(self.root)
    def sizerec(self,current):
        if current is None:
            return 0
        return 1 + self.sizerec(current.left)+ self.sizerec(current.right)

    def export(self, filename="arbol.txt"):

        with open(filename, 'w') as file:
            self._export_recursive(self.root, file)
        print(f"Árbol exportado a {filename}")

    def _export_recursive(self, node, file):
        if node is None:
            file.write("null ")
        else:
            file.write(f"{node.valor} ")
            self._export_recursive(node.left, file)
            self._export_recursive(node.right, file)

    def load(self, filename="arbol.txt"):

        try:
            with open(filename, 'r') as file:

                contenido = file.read()


                lineas = contenido.split('\n')
                datos = []
                for linea in lineas:
                    if not linea.startswith('#') and not linea.startswith('='):
                        datos.extend(linea.split())


            valores = []
            for item in datos:
                if item != "null":
                    try:
                        valores.append(int(item))
                    except ValueError:
                        continue

            # Reconstruir árbol
            self.root = None
            for valor in valores:
                self.insert(valor)

            print(f"✓ Árbol cargado desde {filename}")
            print(f"  Nodos cargados: {len(valores)}")

        except FileNotFoundError:
            print(f"✗ Archivo {filename} no encontrado")
        except Exception as e:
            print(f"✗ Error al cargar: {e}")


if __name__ == '__main__':
    arbol = Arbol()
while True:
    print("------------MENU-------------")
    print("1 - insert")
    print("2 - search")
    print("3 - delete")
    print("4 - order")
    print("5 - height")
    print("6 - size")
    print("7 - export")
    print("8 - help")
    print("9 - exit")
    opcion=input(" ")


    match opcion:
        case "insert":
            value = int(input("insert "))
            arbol.insert(value)

        case "search":
            value = int(input("search "))
            arbol.search(value)
        case "delete":
            value = int(input("delete "))
            arbol.delete(value)
        case "order":
            print("in) INORDEN")
            print("pre) PREORDER")
            print("post) POSTORDER")
            orden = input("Ingrese la orden que desea: ")
            match orden:
                case "in":
                    print("RECORRIDO EN INORDEN")
                    arbol.inorder()
                case "pre":
                    print("RECORRIDO EN PREORDEN")
                    arbol.preorder()
                case "post":
                    print("RECORRIDO EN POSTORDEN")
                    arbol.postorder()
        case "height":
            print(f"Altura del árbol: {arbol.height()}")
        case "size":
            print(f"Tamaño del arbol: {arbol.size()}")
        case "export":
            print("ex) EXPORTAR")
            print("imp) IMPORTAR")
            choice = input("Ingrese la opcion que desea: ")
            match choice:
                case "exp":
                    arbol.export("arbol.txt")
                case "imp":
                    arbol.load("arbol.txt")
        case "help":
            print("\n--- AYUDA ---")
            print("Este programa implementa un árbol binario de búsqueda.")
            print("Características:")
            print("- Los valores menores van a la izquierda")
            print("- Los valores mayores van a la derecha")
            print("\nOperaciones disponibles:")
            print("1. insert: Agrega un nuevo valor al árbol")
            print("2. search: Encuentra un valor en el árbol")
            print("3. delete: Remueve un valor del árbol")
            print("4. order: Muestra los valores en diferente orden")
            print("4.1. in: Izquierda/Raiz/Derecha")
            print("4.2. pre: Raiz/Izquierda/Derecha")
            print("4.3. post: Izquierda/Derecha/Raiz")
            print("5. height: Muestra la altura del árbol")
            print("6. size: Muestra el número de nodos")
            print("7. export: Exporta el árbol a un formato")
            print("7.1. exp: Exporta el arbol a un formato")
            print("7.2. imp: Importa el arbol a un formato")
            print("8. help: Menu de ayuda")
            print("9. exit: Termina el programa")
        case "exit":
            print("Programa terminado")
            break