#include <iostream>
using namespace std;
#include <string>
int main() {
    
    string miArray[]={"David", "Jorge","Carro"};
    int size = sizeof(miArray) / sizeof(miArray[0]);
    for(int i=0; i<size; i++){
        cout<<miArray[i]<<endl;
    }

    return 0;
}
