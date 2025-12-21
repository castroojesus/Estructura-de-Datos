// COLA CON ARRAYS
#include <iostream>
using namespace std;
#define MAXSIZE 5

int queue[MAXSIZE];
int front = -1, rear = -1;

void insertar(){
    int elem;
    cout<<"Ingrese el elemento: ";
    cin>> elem;
    if (rear ==MAXSIZE -1){
        cout<<"OVERFLOW";
        return;
    }
    if (front == -1 && rear == -1){
        front = rear = 0;
    }else{
        rear++;
    }
    queue[rear] = elem;
    cout<<"Elemento insertado correctamente"<<endl;
}

void eliminar(){
    if (front == -1 || front > rear){
        cout<<"UNDERFLOW";
        return;
    }
    int elemento =queue[front];
    if (front == rear){
        front = rear = -1;
    }else{
        front++;
    }
    cout<<"Elemento eliminado"<< elemento <<endl;
}

void mostrar(){
    if (rear == -1 || front == -1 || front >rear){
         cout<<"La cola esta vacia";
    }else{
         cout<<"Elementos de la cola: "<<endl;
         for (int i = front; i <= rear; i++){
             cout<< queue[i] << "\n";
         }
    }
}

int main() {

        int opc = 0;
        
        while (opc != 4){
            cout<<"\n************************MENU QUEUE****************************\n";
            cout<<"==================================================================\n";
            cout<<"1. Insertar elemento en la cola\n";
            cout<<"2. Eliminar elemento de la cola\n";
            cout<<"3. Mostrar la cola\n";
            cout<<"4. Salir\n";
            cout<<"Ingrese su opcion: ";
            cin>> opc;
            
    
        switch(opc){
            case 1:
            insertar();
            break;
            case 2:
            eliminar();
            break;
            case 3:
            mostrar();
            break;
            case 4: 
            cout<<"Saliendo del programa...\n";
            break;
            default:
            cout<<"\nOpcion invalida. Ingrese de nuevo\n";
         }
     }

    return 0;
}