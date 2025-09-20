#include <iostream>
#include <random>
#include <chrono>


using namespace std;

void randomnumber(int a[], int tam){
unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    mt19937 gen(seed);
    uniform_int_distribution<> dis(1, 100);


    for(int i=0;i<tam;i++){
        a[i]=dis(gen);
    }

}

void SelectionSort(int a[], int tam){
 for (int i = 0; i < tam; i++)
    {
        int small=i;
        for (int j = i + 1; j < tam; j++)
        {
           if (a[j]<a[small]){
                small = j;
            }
            
        }
        int temp = a[small];
            a[small] = a[i];
            a[i] = temp;
    }
}

int main()
{
    int arr[15];
    int tam= sizeof(arr)/sizeof(arr[0]);
    randomnumber(arr,tam);
    cout<<"Array Original: "<<endl;
    for (int i=0;i<tam;i++){
        cout<<arr[i]<<" ";
    }
    SelectionSort(arr,tam);
    cout<<"\nArray Ordenado: "<<endl;
    for (int i=0;i<tam;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}
