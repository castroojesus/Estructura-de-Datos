#include <iostream>

using namespace std;

int main()
{
    int mat3d[3][3][3] = {

       {{1,2,3},{4,5,6},{7,8,9}},
       {{10,11,12},{13,14,15},{16,17,18}},
       {{19,20,21},{22,23,24},{25,26,27}}
    };

    int busqueda;

    cout << "Ingresa el valor que deseas buscar: " << endl;
    cin >> busqueda;

    bool encontrado = false;
        for (int i = 0; i < 3 && !encontrado; i++) {
            for (int j = 0; j < 3 && !encontrado; j++) {
                for (int k = 0; k < 3; k++) {
                    if (busqueda == mat3d[i][j][k]) {
                        cout << "El valor " << busqueda << " se encuentra en la posicion ("
                             << i << "," << j << "," << k << ")" << endl;
                        encontrado = true;
                        break;
                    }
                }
            }
        }
        if (!encontrado) {
            cout << "El valor no se encuentra en la matriz." << endl;
        }
        return 0;
}
