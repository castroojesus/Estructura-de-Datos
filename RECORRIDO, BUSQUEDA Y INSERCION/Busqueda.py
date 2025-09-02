miArray = [1,2,3,4,5] #mi array de 5 elementos

print("Escriba el indice del elemento que desea buscar en un rango de 5 posiciones:") #le pregunto al usuario el indice del elemento a buscar
busqueda = int(input()) #variable de input
if busqueda >= len(miArray) or busqueda < 0 : #
    print("Error el indice a buscar es mayor que el rango en el array, intente de nuevo:")
    busqueda = int(input())

for i in range(len(miArray)): #recorrido de array donde si la variable de iteracion es igual a la variable de input escriba el elemento del indice que busca el usuario
    if i == busqueda:
        print("El elemento que se encuentra en el indice ", busqueda, " es: ",miArray[i])
