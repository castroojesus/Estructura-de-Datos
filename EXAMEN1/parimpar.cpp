#include <iostream>

using namespace std;

int main()
{

    int mat[]={1,2,3,4,5,6,7,8,9,10};
    int par=0;
    int impar=0;

    for (int i = 0; i<10;i++){
        if (mat[i]%2==0){
            par+=1;
        }else{
        impar+=1;
        }
    }

    cout << "El total de pares es: " << par<<endl;
    cout<<"El total de impares es: "<<impar<<endl;
    return 0;
}
