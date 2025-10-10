import random

def randomnumber(a):
    for i in range(len(a)):
        a[i] = random.randint(1, 100)

def printarray(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()


def ShellSort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a


array = [0] * 15
randomnumber(array) 
longitud = len(array)
print("Arreglo Original: ")
printarray(array)
ShellSort(array)  
print("Array Ordenado:")
printarray(array)        
