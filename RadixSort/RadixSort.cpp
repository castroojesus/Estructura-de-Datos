#include <iostream>
#include <random>
#include <chrono>
#include <vector>
#include <algorithm>


using namespace std;

void randomnumber(vector<int>&arr){
unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    mt19937 gen(seed);
    uniform_int_distribution<> dis(1, 100);


    for(int i=0;i<arr.size();i++){
        arr[i]=dis(gen);
    }

}

void counting_sort(vector<int>& a, int exp) {
    int n = a.size();
    vector<int> output(n);
    vector<int> count(10, 0);

    // Contar la frecuencia de cada dígito
    for (int i = 0; i < n; i++) {
        int index = (a[i] / exp) % 10;
        count[index]++;
    }

    // Calcular las posiciones acumuladas
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // Construir el array de salida (estable)
    for (int i = n - 1; i >= 0; i--) {
        int index = (a[i] / exp) % 10;
        output[count[index] - 1] = a[i];
        count[index]--;
    }

    // Copiar el array ordenado al original
    for (int i = 0; i < n; i++) {
        a[i] = output[i];
    }
}

void radix_sort(vector<int>& a) {
    if (a.empty()) return;
    
    int max1 = *max_element(a.begin(), a.end());

    int exp = 1;
    while (max1 / exp > 0) {
        counting_sort(a, exp);
        exp *= 10;
    }
}

int main()
{
    vector <int>arr(15);
    
    randomnumber(arr);
    cout<<"Array Original: "<<endl;
    for (size_t i=0;i<arr.size();i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    radix_sort(arr);
    cout<<"Array Ordenado con Bucket Sort: "<<endl;
    for (int i=0;i<arr.size();i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    return 0;
}
