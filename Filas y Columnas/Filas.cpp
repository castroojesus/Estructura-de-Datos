#include <iostream>
using namespace std;

int main(){
    const int r = 3, c = 3;
    
    int TwoDArr[r][c] = {{1,2,3},{4,5,6},{7,8,9}};
    
    
    
    cout<<"Los elementos del array bidimensional son: "<<endl;
    
    for(int x = 0; x < r; x++) {
        for(int y = 0; y < c; y++) {
            cout << TwoDArr[x][y] << " ";
        }
        cout << endl;
    }
    
    cout << "\nLos elementos del array unidimensional son: "<<endl;
   for(int x = 0; x < r; x++) {
        for(int y = 0; y < c; y++) {
            cout << TwoDArr[x][y] << " ";
        }
        
    }
    
    return 0;
}
