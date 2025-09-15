for i in range(15):
    array[i]=random.randint(1,100)
    
print("Array antes de ordenar: ")
for i in range(15):
    print(array[i], end=" ")
    
mayor =0
for i in range(15):
    for j in range(0,15-i-1):
        if array[j]>array[j+1]:
            mayor = array[j]
            array[j] = array[j+1]
            array[j+1] = mayor

print("\nArray despues de ordenar: ")
for i in range(15):
    print(array[i], end=" ")
