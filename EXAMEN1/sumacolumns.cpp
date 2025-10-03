#include <iostream>

using namespace std;

int main()
{

    int mat2d[3][3]={{1,2,3},{4,5,6},{7,8,9}};
    int suma=0;

    for(int j=0;j<3;j++){
        for(int i=0;i<3;i++){
            suma+=mat2d[i][j];

        }
        cout<<"La suma de la columna es: "<<suma<<endl;
        suma=0;
    }

    return 0;
}
