#include <iostream>
using namespace std;

struct Node {
    int data;           //dato del nodo
    Node* next;         //direccion al siguiente nodo
};

Node* top = nullptr;    //puntero a tope de pila

//funcion para insertar en pila
void push(int item) {
    Node* newNode = new Node();    //crea un nodo
    newNode->data = item;          //asigna el dato
    newNode->next = top;           //el nuevo nodo apunta al anterior tope
    top = newNode;                 //el nuevo nodo es ahora el tope
    cout << "Elemento insertado: " << item << endl;
}

//funcion para eliminar un elemento o extraer
int pop() {
    if (top == nullptr) {          //si la pila esta vacia
        cout << "STACK UNDERFLOW" << endl;
        return -1;
    }
    Node* temp = top;              //guarda el nodo del tope
    int valor = top->data;         //guarda el dato
    top = top->next;               //mueve el tope al siguiente nodo
    delete temp;                   //libera la memoria del nodo eliminado
    return valor;
}

//funcion para ver el elemento superior 
int peek() {
    if (top == nullptr) {         //si esta vacia
        cout << "PILA VACIA" << endl;
        return -1;
    }
    return top->data;             //retorna el valor del tope
}

//funcion para ver si la pila esta vacia
bool isEmpty() {
    return top == nullptr;        //retorna true si el tope es nullptr, o sea que esta vacia
}

int main() {
    int choice = 0;
    while (choice != 5) {
        cout << "\n\n*********Menu Pila*********\n";
        cout << "1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Salir\n";
        cout << "Ingrese su opción: ";
        if (!(cin >> choice)) {
            cin.clear(); cin.ignore(10000, '\n'); choice = 0;
        }
        switch(choice) {
            case 1: {
                int valor;
                cout << "Ingrese el valor a insertar: ";
                cin >> valor;
                push(valor);
                break;
            }
            case 2: {
                int valor = pop();
                if (valor != -1) cout << "Elemento extraído: " << valor << endl;
                break;
            }
            case 3: {
                int valor = peek();
                if (valor != -1) cout << "Elemento superior: " << valor << endl;
                break;
            }
            case 4:
                cout << (isEmpty() ? "La pila está vacía" : "La pila NO está vacía") << endl;
                break;
            case 5:
                cout << "Saliendo del programa..." << endl;
                break;
            default:
                cout << "Por favor, introduzca una opción válida\n";
        }
    }
    return 0;
}