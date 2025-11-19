#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

class CircularLinkedList {
private:
    Node* last;
   
public: 
    CircularLinkedList() : last(nullptr) {}

    void insertbegin() {
        int value;
        cout << "Ingrese un valor: ";
        cin >> value;

        Node* newNode = new Node();
        newNode->data = value;
        
        if (last == nullptr) {
            last = newNode;
            last->next = last;
        } else {
            
            newNode->next=last->next;
            
            last->next = newNode;
        }
    }
    
    void insertend(){
        int value;
        cout << "Ingrese un valor: ";
        cin >> value;

        Node* newNode = new Node();
        newNode->data = value;
        if (last == nullptr) {
            last = newNode;
            last->next = last;
        } else {
            
            newNode->next=last->next;
            
            last->next = newNode;
            last=newNode;
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
        Node* actual=last->next;
        if (last == nullptr) {
            last = newNode;
            last->next = last;
        } else {
            for (int i=0;i<pos-1;i++){
                if (actual == last) {
                    break; // Llegamos al final antes de la posición deseada, insertamos al final.
                }
                actual = actual->next;
            }
            newNode->next=actual->next;
            
            actual->next = newNode;
            if (actual == last) {
                last = newNode;
            }
        }
    }

    void deletebegin() {
        if (last == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* temp = last->next;
        if (last->next == last) {
            last = nullptr;
        } else {
            last->next = temp->next;
        }
        delete temp;
    }

    void deleteend() {
        if (last == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* temp = last->next;
        if (last->next == last) {
            delete last;
            last = nullptr;
        } else {
            while (temp->next != last) {
                temp = temp->next;
            }
            temp->next = last->next;
            delete last;
            last = temp;
            cout<< "Elemento eliminado desde el final" << endl;
        }
    }

    void deleteRandom() {
        if (last == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* current = last->next;
        Node* previous = last;
        int pos;
        cout << "Ingresa la posicion: ";
        cin >> pos;
        for (int i = 0; i < pos; i++) {
            if (current == last) {
                cout << "La posicion no existe" << endl;
                return;
            }
            previous = current;
            current = current->next;
        }
        previous->next = current->next;
        if (current == last) {
            last = previous;
        }
        delete current;
        cout << "Elemento eliminado desde la posicion " << pos << endl;
    }

    void search() {
        if (last == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        int value;
        cout << "Ingrese el valor a buscar: ";
        cin >> value;
        Node* temp = last->next;
        int pos = 0;
        do {
            if (temp->data == value) {
                cout << "Valor " << value << " encontrado en la posicion " << pos << endl;
                return;
            }
            temp = temp->next;
            pos++;
        } while (temp != last->next);
        cout << "Valor " << value << " no encontrado en la lista" << endl;
    }

    void display() {
        if (last == nullptr) {
            cout << "La lista esta vacia" << endl;
            return;
        }
        Node* temp = last->next;
        cout << "Lista Circular: ";
        do {
            cout << temp->data << "-> ";
            temp = temp->next;
        } while (temp != last->next);
        cout <<"inicio"<< endl;
    }

    
};

int main() {
    CircularLinkedList cll;
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
                cll.insertbegin();
                break;
            case 2:
                cll.insertend();
                break;
            case 3:
                cll.insertrandom();
            case 4:
                cll.deletebegin();
                break;
            case 5:
                cll.deleteend();
                break;
            case 6:
                cll.deleteRandom();
                break;
            case 7:
            
                cll.search();
                break;
            case 8:
                cll.display();
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
