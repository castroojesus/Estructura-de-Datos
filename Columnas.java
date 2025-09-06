 public class Columnas {
    public static void main(String[] args) {
        final int r=3;
        final int c=3;

        int[] arr=new int[r*c];
        int[][] TwoDArray={{1,2,3},{4,5,6},{7,8,9}};
        int k=0;

        
        for(int y=0;y<c;y++){
            for(int x=0;x<r;x++){
                k=y*r+x;
                arr[k]=TwoDArray[x][y];
                k=k+1;
            }
        }
        System.out.println("Los elementos del array bidimensional son: ");
         for(int x=0;x<r;x++){
            for(int y=0;y<c;y++){
                System.out.print(TwoDArray[x][y]+" ");
            }
            System.out.println();
        }

        System.out.println("\nLos elementos del array unidimensional son: ");
        for(int y=0;y<c;y++){
            for(int x=0;x<r;x++){
                System.out.println(arr[y*r+x]+" ");
            }
           
        }

    }
    
}
