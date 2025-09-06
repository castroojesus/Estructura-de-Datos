#include <iostream>
using namespace std;

int main(){
    const int r = 3, c = 3;
    int arr[r * c];
    int k=0;
    int TwoDArr[r][c] = {{1,2,3},{4,5,6},{7,8,9}};
    
    
    for(int x = 0; x < r; x++) {
        for(int y = 0; y < c; y++) {
            k=x*r+y;
            arr[k] = TwoDArr[x][y];
            k=k+1;
        }
    }
    cout<<"Los elementos del array bidimensional son: "<<endl;
    
    for(int x = 0; x < r; x++) {
        for(int y = 0; y < c; y++) {
            cout << TwoDArr[x][y] << " ";
        }
        cout << endl;
    }
    
    cout << "\nLos elementos del array unidimensional son: "<<endl;
    for(int i = 0; i < r * c; i++) {
        cout << arr[i] << " ";
    }
    
    return 0;
}
