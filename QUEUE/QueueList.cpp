#include <iostream>
using namespace std;

struct Nodo {
    int dato;
    Nodo* siguiente;
};

Nodo* front = nullptr;
Nodo* rear = nullptr;

void insertar() {
    int elem;
    cout << "Ingrese el elemento: ";
    cin >> elem;

    Nodo* nuevo = new Nodo();
    nuevo->dato = elem;
    nuevo->siguiente = nullptr;

    if (front == nullptr && rear == nullptr) {
        front = rear = nuevo;
    } else {
        rear->siguiente = nuevo;
        rear = nuevo;
    }

    cout << "Elemento insertado correctamente\n";
}

void eliminar() {
    if (front == nullptr) {
        cout << "UNDERFLOW\n";
        return;
    }

    Nodo* temp = front;
    int elemento = temp->dato;

    front = front->siguiente;
    if (front == nullptr) {
        rear = nullptr;
    }

    delete temp;
    cout << "Elemento eliminado: " << elemento << endl;
}

void mostrar() {
    if (front == nullptr) {
        cout << "La cola está vacía\n";
        return;
    }

    cout << "Elementos de la cola:\n";
    Nodo* actual = front;
    while (actual != nullptr) {
        cout << actual->dato << "\n";
        actual = actual->siguiente;
    }
}

int main() {
    int opc = 0;

    while (opc != 4) {
        cout << "\n*************** MENU QUEUE ***************\n";
        cout << "1. Insertar elemento en la cola\n";
        cout << "2. Eliminar elemento de la cola\n";
        cout << "3. Mostrar la cola\n";
        cout << "4. Salir\n";
        cout << "Ingrese su opción: ";
        cin >> opc;

        switch (opc) {
            case 1: insertar(); break;
            case 2: eliminar(); break;
            case 3: mostrar(); break;
            case 4: cout << "Saliendo del programa...\n"; break;
            default: cout << "Opción inválida. Ingrese de nuevo\n";
        }
    }

    return 0;
}