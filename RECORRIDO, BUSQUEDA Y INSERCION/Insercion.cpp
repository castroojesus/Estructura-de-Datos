
using namespace std;

int main() {
  
  int miArray[]={1,2,3,4,5};
  int posicion = 0;
  int nuevo = 22;
  
  cout<<"Los elementos del array antes de insercion son:"<<endl;
  for(int i=0;i<5;i++){
      cout<<miArray[i];
      cout<<"\n";
  }
  
  for(int i =4;i>posicion;i--){
      miArray[i]=miArray[i-1];
  }
  
  miArray[posicion]=nuevo;
  
  cout<<"Los elementos del array despues de insercion son:"<<endl;
  for(int i=0;i<5;i++){
      cout<<miArray[i];
      cout<<"\n";
  }

    return 0;
}
