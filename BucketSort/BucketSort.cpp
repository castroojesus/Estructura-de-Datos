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

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void bucketSort(int arr[], int n) {
    const int bucketCount = 10;
    int maxValue = 100; 
    int bucketRange = (maxValue / bucketCount) + 1;

    
    int** buckets = new int*[bucketCount];
    int* bucketSizes = new int[bucketCount]();
    for (int i = 0; i < bucketCount; i++) {
        buckets[i] = new int[n]; 
    }

    
    for (int i = 0; i < n; i++) {
        int bucketIndex = arr[i] / bucketRange;
        buckets[bucketIndex][bucketSizes[bucketIndex]++] = arr[i];
    }

    
    int index = 0;
    for (int i = 0; i < bucketCount; i++) {
        insertionSort(buckets[i], bucketSizes[i]);
        for (int j = 0; j < bucketSizes[i]; j++) {
            arr[index++] = buckets[i][j];
        }
        delete[] buckets[i]; 
    }

    delete[] buckets;
    delete[] bucketSizes;
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
    bucketSort(arr, tam);
    cout<<"Array Ordenado con Bucket Sort: "<<endl;
    for (int i=0;i<tam;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}