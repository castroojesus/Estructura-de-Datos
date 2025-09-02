#include <iostream>

using namespace std;

int main() {
  
  int miArray[]={1,2,3,4,5};
  int busqueda;
  
  cout<<"Escriba el indice del elemento que desea buscar en un rango de 4 posiciones:"<<endl;
  cin>>busqueda;
  
  if(busqueda>=5||busqueda<0){
      cout<<"Error el indice a buscar es mayor que el rango en el array, intente de nuevo:"<<endl;
    cin>>busqueda;
  }
  
  for(int i=0;i<5;i++){
      if(i==busqueda){
          cout<<"El elemento que se encuentra en el indice "<<busqueda<<" es: "<<miArray[i];
      }
  }
  
    return 0;
}
