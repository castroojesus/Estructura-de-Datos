#include <iostream>
#include <random>
#include <chrono>


using namespace std;

int swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
    return 0;
}

int partition(int a[], int low, int high){
    int pivot = a[high];
    int i = (low - 1);
    for (int j = low; j < high; j++)
    {
        if (a[j] <= pivot)
        {
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i + 1], a[high]);
    return (i + 1);
}

int quickSort(int a[], int low, int high){
    if (low < high)
    {
        int pi = partition(a, low, high);
        quickSort(a, low, pi - 1);
        quickSort(a, pi + 1, high);
    }
    return 0;
}

void randomnumber(int a[], int tam){
unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    mt19937 gen(seed);
    uniform_int_distribution<> dis(1, 100);


    for(int i=0;i<tam;i++){
        a[i]=dis(gen);
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
    quickSort(arr,0,tam-1);
    cout<<"\nArray Ordenado: "<<endl;
    for (int i=0;i<tam;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}