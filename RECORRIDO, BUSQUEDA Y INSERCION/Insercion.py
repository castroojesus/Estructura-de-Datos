miArray = [1,2,3,4,5] #mi array de 5 elementos
posicion=3 #la posicion donde quiero añadir el nuevo elemento
nuevo=15 #el valor del nuevo elemento
print("Recorrido de array antes de insercion: ",end="")
for i in range(len(miArray)):
    print(miArray[i])

print("Recorrido de array despues de insercion: ",end="")
for i in range(len(miArray)-1,posicion,-1): #aqui digo que va a iterar desde el final del array, hasta el numero de la posicion en decremento
    miArray[i]=miArray[i-1] #aqui digo que el valor de i ahora va a valer i -1, osea que lo que hay en la posicion 4 ahora va a ser lo que hay en la 3
    
miArray[posicion]=nuevo #asigno el valor del nuevo elemento en la posicion
for i in range(len(miArray)):
    print(miArray[i])
