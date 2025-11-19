#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node* prev;
};

class DoublyCircularLinkedList {
private:
    Node* head;
    Node* tail; 
public:
    DoublyCircularLinkedList() : head(nullptr), tail(nullptr) {}
    void insertbegin() {
        int value;
        cout << "Ingrese un valor: ";
        cin >> value;

        Node* newNode = new Node();
        newNode->data = value;

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
            newNode->next = newNode;
            newNode->prev = newNode;
        } else {
            newNode->next = head;
            newNode->prev = tail;
            head->prev = newNode;
            tail->next = newNode;
            head = newNode;
        }
    }
    void insertend(){
        int value;
        cout << "Ingrese un valor: ";
        cin >> value;

        Node* newNode = new Node();
        newNode->data = value;

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
            newNode->next = newNode;
            newNode->prev = newNode;
        } else {
            newNode->next = head;
            newNode->prev = tail;
            tail->next = newNode;
            head->prev = newNode;
            tail = newNode;
        }
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

        if (head == nullptr) {
            head = newNode;
            tail = newNode;
            newNode->next = newNode;
            newNode->prev = newNode;
        } else {
            Node* current = head;
            for (int i = 0; i < pos; i++) {
                current = current->next;
                if (current == head) {
                    break; 
                }
            }
            newNode->next = current;
            newNode->prev = current->prev;
            current->prev->next = newNode;
            current->prev = newNode;

            if (current == head && pos == 0) {
                head = newNode; 
            }
            if (current == head) {
                tail = newNode; 
            }
        }
    }
    void deletebegin(){
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }

        if (head == tail) {
            delete head;
            head = nullptr;
            tail = nullptr;
        } else {
            Node* temp = head;
            head = head->next;
            head->prev = tail;
            tail->next = head;
            delete temp;
        }
        cout<< "Elemento eliminado desde el inicio" << endl;
    }
    void deleteend(){
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }

        if (head == tail) {
            delete head;
            head = nullptr;
            tail = nullptr;
        } else {
            Node* temp = tail;
            tail = tail->prev;
            tail->next = head;
            head->prev = tail;
            delete temp;
        }
        cout<< "Elemento eliminado desde el final" << endl;
    }
    void deleteRandom(){
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* current = head;
        int pos;
        cout << "Ingresa la posicion: ";
        cin >> pos;
        for (int i = 0; i < pos; i++) {
            current = current->next;
            if (current == head) {
                cout << "La posicion no existe" << endl;
                return;
            }
        }
        current->prev->next = current->next;
        current->next->prev = current->prev;

        if (current == head) {
            head = current->next; 
        }
        if (current == tail) {
            tail = current->prev; 
        }
        if (head == nullptr) {
            tail = nullptr; 
        }
        delete current;
        cout << "Elemento eliminado desde la posicion " << pos << endl;
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
        do {
            if (temp->data == value) {
                cout << "Valor " << value << " encontrado en la posicion " << pos << endl;
                return;
            }
            temp = temp->next;
            pos++;
        } while (temp != head);
        cout << "Valor " << value << " no encontrado en la lista" << endl;
    }
    void display() {
        if (head == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* temp = head;
        cout << "Lista Doble Circular: ";
        do {
            cout << temp->data << " <-> ";
            temp = temp->next;
        } while (temp != head);
        cout <<"inicio"<< endl;
    }
};

int main() {
    DoublyCircularLinkedList dcll;
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
                dcll.insertbegin();
                break;
            case 2:
                dcll.insertend();
                break;
            case 3:
                dcll.insertrandom();
                break;
            case 4:
                dcll.deletebegin();
                break;
            case 5:
                dcll.deleteend();
                break;
            case 6:
                dcll.deleteRandom();
                break;
            case 7:
                dcll.search();
                break;
            case 8:
                dcll.display();
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