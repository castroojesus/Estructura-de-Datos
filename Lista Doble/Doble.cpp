#include <iostream>
using namespace std;
struct Node {
    int data;
    Node* next;
    Node* prev;
};

class DoublyLinkedList {
private:
    Node* head;
    Node* tail;
public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}
    void insertbegin() {
        int value;
        cout << "Ingrese un valor: ";
        cin >> value;

        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = head;
        newNode->prev = nullptr;

        if (head != nullptr) {
            head->prev = newNode;
        } else {
            tail = newNode; // Si la lista estaba vacía, el nuevo nodo es también la cola
        }
        head = newNode;
    }

    void insertend(){
        int value;
        cout << "Ingrese un valor: ";
        cin >> value;

        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = nullptr;
        newNode->prev = tail;

        if (tail != nullptr) {
            tail->next = newNode;
        } else {
            head = newNode; 
        }
        tail = newNode;
    }

    void insertrandom(){
        int value;
        int pos;
        cout << "Ingrese un valor: ";
        cin >> value;
        cout << "Ingrese la posicion donde desea insertar: ";
        cin >> pos;

        Node* newNode = new Node();
        newNode->data = value;

        if (pos <= 0 || head == nullptr) {
            insertbegin();
            return;
        }

        Node* current = head;
        for (int i = 0; i < pos - 1; i++) {
            if (current->next == nullptr) {
                insertend();
                return;
            }
            current = current->next;
        }

        newNode->next = current->next;
        newNode->prev = current;

        if (current->next != nullptr) {
            current->next->prev = newNode;
        } else {
            tail = newNode; 
        }
        current->next = newNode;
        cout<< "Elemento insertado en la posicion " << pos << endl;
    }
    void deletebegin(){
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* temp = head;
        head = head->next;
        if (head != nullptr) {
            head->prev = nullptr;
        } else {
            tail = nullptr; 
        }
        delete temp;
        cout << "Elemento eliminado desde el inicio" << endl;
    }
    void deleteend(){
        if (tail == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* temp = tail;
        tail = tail->prev;
        if (tail != nullptr) {
            tail->next = nullptr;
        } else {
            head = nullptr; 
        }
        delete temp;
        cout<< "Elemento eliminado desde el final" << endl;
    }
    void deleteRandom(){
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        int pos;
        cout << "Ingresa la posicion: ";
        cin >> pos;

        Node* current = head;
        for (int i = 0; i < pos; i++) {
            if (current == nullptr) {
                cout << "La posicion no existe" << endl;
                return;
            }
            current = current->next;
        }

        if (current->prev != nullptr) {
            current->prev->next = current->next;
        } else {
            head = current->next; 
        }

        if (current->next != nullptr) {
            current->next->prev = current->prev;
        } else {
            tail = current->prev; 
        }

        delete current;
    }
    void search(){
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        int value;
        cout << "Ingrese el valor a buscar: ";
        cin >> value;

        Node* temp = head;
        int pos = 0;
        while (temp != nullptr) {
            if (temp->data == value) {
                cout << "Valor " << value << " encontrado en la posicion " << pos << endl;
                return;
            }
            temp = temp->next;
            pos++;
        }
        cout << "Valor " << value << " no encontrado en la lista" << endl;
    }


    void display() {
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* temp = head;
        cout << "Lista Doble: ";
        while (temp != nullptr) {
            cout << temp->data << " <-> ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }
};

int main() {
    DoublyLinkedList dll;
    int choice;

    do {
        cout << "1. Insertar al inicio" << endl;
        cout << "2. Insertar al final" << endl;
        cout << "3. insertar en posicion aleatoria" << endl;
        cout << "4. Eliminar al inicio" << endl;
        cout << "5. Eliminar al final" << endl;
        cout << "6. Eliminar desde posicion especifica" << endl;
        cout << "7. Buscar" << endl;
        cout << "8. Mostrar lista" << endl;
        cout << "9. Salir" << endl;
        cout << "Ingrese su opcion: ";
        cin >> choice;

        switch (choice) {
            case 1:
                dll.insertbegin();
                break;
            case 2:
                dll.insertend();
                break;
            case 3:
                dll.insertrandom();
                break;
            case 4:
                dll.deletebegin();
                break;
            case 5:
                dll.deleteend();
                break;
            case 6:
                dll.deleteRandom();
                break;
            case 7:
            
                dll.search();
                break;
            case 8:
                dll.display();
                break;
            case 9:
                cout << "Saliendo..." << endl;
                break;
            default:
                cout << "Opcion invalida. Intente de nuevo." << endl;
        }
    } while (choice != 9);

    return 0;
}