#include <iostream>
#include <random>
#include <chrono>
using namespace std;

int main()
{
    int array[15];
    unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    mt19937 gen(seed);
    uniform_int_distribution<> dis(1, 100);

    for(int i=0;i<15;i++){
        array[i]=dis(gen);
    }

    cout<<"Array antes de ordenar: "<<endl;
    for(int i=0;i<15;i++){
        cout<<array[i]<<" ";
    }

    int mayor=0;
    int n = 15;
for(int i = 0; i < n - 1; i++) {           // n-1 pasadas
    for(int j = 0; j < n - i - 1; j++) {   // Comparar elementos adyacentes
        if(array[j] > array[j + 1]) {
            // Intercambiar
            mayor = array[j];
            array[j] = array[j + 1];
            array[j + 1] = mayor;
        }
    }
}

    cout<<"\nArray despues de ordenar: "<<endl;
    for(int i=0;i<15;i++){
        cout<<array[i]<<" ";
    }

    return 0;
}
