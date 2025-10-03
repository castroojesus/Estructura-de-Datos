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

void heapify(int arr[], int n, int i) {
    int largest = i; 
    int left = 2 * i + 1; 
    int right = 2 * i + 2; 

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
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
    cout<<endl;
    heapSort(arr, tam);
    cout<<"Array Ordenado con Heap Sort: "<<endl;
    for (int i=0;i<tam;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}