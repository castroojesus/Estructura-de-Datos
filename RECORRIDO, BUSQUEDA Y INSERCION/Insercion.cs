using System;

public class Insercion
{
    public static void Main(string[] args){
        
         int[] miArray = {1,2,3,4,5};
        int posicion=2;
        int nuevo=11;
        
        Console.WriteLine("Los elementos del array antes de insercion son: ");
        for(int i=0;i<5;i++){
            Console.WriteLine(miArray[i]);
        }
        
        for(int i = 4;i>posicion;i--){
            miArray[i]=miArray[i-1];
        }
        
        miArray[posicion]=nuevo;
        
        Console.WriteLine("Los elementos del array despues de insercion son: ");
        for(int i=0;i<5;i++){
            Console.WriteLine(miArray[i]);
        }
        
    }
}
