r=3;c=3
arr=[0]*r*c
TwoDArr=[[1,2,3],[4,5,6],[7,8,9]];
k=0
for y in range(c): #inicio con las columnas y luego con las filas
    for x in range(r):
        k=y*r+x; #la formula cambia 
        arr[k]=TwoDArr[x][y]
        k=k+1
print("Los elementos del array bidimensional son: ")
for row in TwoDArr:
    for ele in row:
        print(ele,end=" ")
    print()
print("\nLos elementos del array unidimensional son: ")
for x in range(len(arr)):
    print(arr[x],end=" ")
