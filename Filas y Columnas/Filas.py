TwoDArr=[[1,2,3],[4,5,6],[7,8,9]];


print("Los elementos del array bidimensional son: ")
for row in TwoDArr:
    for ele in row:
        print(ele,end=" ")
    print()

filas=len(TwoDArr)
columnas=len(TwoDArr[0])

print("\nLos elementos del array unidimensional son: ")
for x in range(filas):
    for y in range(columnas):
        print((TwoDArr[x][y]),end=" ")
