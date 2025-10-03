import random

def randomnumber(a):
    for i in range(len(a)):
        a[i] = random.randint(1, 100)

def printarray(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()

def heapify(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[largest]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)

def HeapSort(a):
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
array = [0] * 15
randomnumber(array) 
longitud = len(array)
print("Arreglo Original: ")
printarray(array)
HeapSort(array)
print("Array Ordenado:")
printarray(array)