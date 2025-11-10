#include <iostream>
#include <cstdlib>
using namespace std;

struct node {
    int data;
   struct node *next;
};

struct node *head;

void insertbeg();
void insertend();
void randominsert();
void deletebeg();
void deleteend();
void randomdelete();
void display();
void search();

int main() {
    int choice = 0;
    while (choice != 9) {
        cout << "\n*********Main Menu*********\n";
        cout << "1. Insert at beginning\n";
        cout << "2. Insert at end\n";
        cout << "3. Insert at random location\n";
        cout << "4. Delete from beginning\n";
        cout << "5. Delete from end\n";
        cout << "6. Delete from random location\n";
        cout << "7. Display\n";
        cout << "8. Search\n";
        cout<<"9. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice) {
            case 1:
                insertbeg();
                break;
            case 2:
                insertend();
                break;
            case 3:
                randominsert();
                break;
            case 4:
                deletebeg();
                break;
            case 5:
                deleteend();
                break;
            case 6:
                randomdelete();
                break;
            case 7:
                display();
                break;
            case 8:
                search();
                break;
            case 9:
                exit(0);
            default:
                cout << "Invalid choice! Please try again.\n";
        }
    }
    return 0;
}

void insertbeg() {
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    int item;
    if (newnode == NULL) {
        cout << "OVERFLOW\n";
        
    }else{
         cout << "Ingresa un elemento: ";
    cin >> item;
    newnode->data = item;
    newnode ->next = head;
    head = newnode;
    cout << "Elemento insertado\n";
    }
   
}

void insertend() {
    struct node *newnode,*temp;
    newnode = (struct node *)malloc(sizeof(struct node));
    int item;
    if (newnode == NULL) {
        cout << "OVERFLOW\n";
        
    }else{
         cout << "Ingresa un elemento: ";
    cin >> item;
    newnode->data = item;
    
    if (head == NULL) {
        newnode->next = NULL;
        head = newnode;
        cout << "Elemento insertado\n";
    } else {
       temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newnode;
        newnode->next = NULL;
        cout << "Elemento insertado\n";
    }
    }
   
}

void randominsert() {
    struct node *newnode, *temp;
    newnode = (struct node *)malloc(sizeof(struct node));
    int item, pos, i;
    if (newnode == NULL) {
        cout << "OVERFLOW\n";
        
    }else{
         cout << "Ingresa un elemento: ";
        cin >> item;
        newnode->data = item;
        cout << "Ingresa la posicion: ";
        cin >> pos;
    
        temp = head;
        for (i = 0; i < pos -1; i++) {
            if (temp == NULL) {
                cout << "La posicion no existe\n";
                return;
            }
            temp = temp->next;
        }
        newnode->next = temp->next;
        temp->next = newnode;
        cout << "Elemento insertado\n";
    
    }
   
}

void deletebeg() {
    struct node *newNode;
    if (head == NULL) {
        cout << "La lista esta vacia\n";
        
    }else{
         newNode = head;
    head = newNode->next;
    delete newNode;
    cout << "Elemento eliminado desde el principio\n";
    }
   
}

void deleteend() {
    struct node *newNode, *temp;
    if (head == NULL) {
        cout << "La lista esta vacia\n";
        
    }else if(head->next == NULL){
        
     
        delete head;
        head = NULL;
        
        cout << "Solo se elimino un nodo de la lista\n";
        return;
    }
    else{
            newNode = head;
        while (newNode->next != NULL) {
        temp = newNode;
        newNode = newNode->next;
        }
        temp->next = NULL;
        delete newNode;
        cout << "Elemento eliminado desde el final\n";
    
    }
   
   
}

void randomdelete() {
    struct node *newNode, *temp;
    int pos, i;
   
    cout << "Ingresa la posicion: ";
    cin >> pos;
    newNode = head;
    for (i = 0; i < pos; i++) {
        if (newNode == NULL) {
            cout << "La posicion no existe\n";
            return;
        }
        temp = newNode;
        newNode = newNode->next;
    }
    temp->next = newNode->next;
    delete newNode;
    cout << "Elemento eliminado desde la posicion " << pos+1 << "\n";
    
   
}

void display() {
    struct node *newNode;
    newNode = head;
    if (newNode == NULL) {
        cout << "La lista esta vacia\n";
        
    }else{

    cout << "Elementos en la lista: ";
    while (newNode != NULL) {
        cout << newNode->data << " ";
        newNode = newNode->next;
    }
    cout << "\n";
    }
   
}

void search() {
    struct node *newNode;
    int item, pos = 0, flag;
    if (head == NULL) {
        cout << "La lista esta vacia\n";
        
    }else{
         cout << "Ingresa el elemento a buscar: ";
    cin >> item;
    newNode = head;
    while (newNode != NULL) {
        if (newNode->data == item) {
            cout << "Elemento " << item << " encontrado en la posicion " << pos << "\n";
            flag = 0;
            
        }else{
            flag = 1;
        }
        newNode = newNode->next;
        pos++;
    }
    if (flag == 1) {
        cout << "Elemento no encontrado en la lista\n";
    }
    }
   
}