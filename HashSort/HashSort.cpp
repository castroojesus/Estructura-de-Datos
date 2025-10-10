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

void shellSort(int arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
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
    shellSort(arr, tam);
    cout<<"Array Ordenado con Hash Sort: "<<endl;
    for (int i=0;i<tam;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}