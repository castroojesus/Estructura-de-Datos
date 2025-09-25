import random

def randomnumber(a):
    for i in range(len(a)):
        a[i] = random.randint(1, 100)

def printarray(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def part(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            swap(a, i, j)
    swap(a, i + 1, high)
    return i + 1

def QuickSort(a, low, high):
    if low < high:
        pi = part(a, low, high)
        QuickSort(a, low, pi - 1)
        QuickSort(a, pi + 1, high)

array = [0] * 15
randomnumber(array)
longitud = len(array)
print("Arreglo Original: ")
printarray(array)
QuickSort(array, 0, longitud - 1)
print("Array Ordenado:")
printarray(array)