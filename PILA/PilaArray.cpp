/PILA
#include <iostream>
#define MAX_SIZE 100
using namespace std;

int stack[MAX_SIZE];      //arreglo de la pila
int top = -1;             //elemento del tope de la pila

//funcion para insertar un elemento en la pila
void push(int item){
    if (top == MAX_SIZE -1){   //si la pila está llena
        cout<<"STACK OVERFLOW"<<endl;
        return;
    }  //sino:
    stack[++top] = item;          //incrememta el indice y agrega el elemento a la pila
}

//funcion para elimina run elemento o sacar
int pop (){
    if (top == -1){          //si la pila esta vacia
        cout<<"STACK UNDERFLOW"<<endl;            //underflow
        return -1;
    }
    return stack[top--];
}

//funcion para ver el elemento superior sin eliminarlo
int peek(){
if (top == -1){         //si esta vacia
    cout<<"PILA VACIA"<<endl;
    return -1;
    }
    return stack[top]; //retorna el valor del tope
}

//funcion para ver si la pila esta vacia
bool isEmpty(){
   return top == -1;    //retorna true si la pila es -1, o sea que esta vacia 
}

//funcion para ver si esta llena
bool isFull(){
    return top == MAX_SIZE -1;         //retorna true si esta llena, si el indice sup es igual al tamao maximo menos uno
}

int main() {
    int choice = 0;
    while (choice != 6) {
        cout << "\n\n*********Menu Pila*********\n";
        cout << "1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Verificar si está llena\n6. Salir\n";
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
                cout << (isFull() ? "La pila está llena" : "La pila NO está llena") << endl;
                break;
            case 6:
                cout << "Saliendo del programa..." << endl;
                break;
            default:
                cout << "Por favor, introduzca una opción válida\n";
        }
    }
    return 0;
}