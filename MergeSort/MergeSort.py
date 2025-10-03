import random

def randomnumber(a):
    for i in range(len(a)):
        a[i] = random.randint(1, 100)

def printarray(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print()

def merge(a, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = a[left + i]

    for j in range(0, n2):
        R[j] = a[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def MergeSort(a, left, right):
    if left < right:
        mid = (left + right) // 2
        MergeSort(a, left, mid)
        MergeSort(a, mid + 1, right)
        merge(a, left, mid, right)

array = [0] * 15
randomnumber(array)
longitud = len(array)
print("Arreglo Original: ")
printarray(array)
MergeSort(array, 0, longitud - 1)
print("Array Ordenado:")
printarray(array)