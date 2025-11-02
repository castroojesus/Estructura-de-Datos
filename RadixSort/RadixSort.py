import random

def randomnumber(a):
    for i in range(len(a)):
     a[i]=random.randint(1,100)
def printarray(a):
   for i in range(len(a)):
     print(a[i], end=" ")

def counting_sort_for_radix(a, exp):
    n = len(a)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (a[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (a[i] // exp) % 10
        output[count[index] - 1] = a[i]
        count[index] -= 1

    for i in range(n):
        a[i] = output[i]

def radix_sort(a):
    max1 = max(a)

    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(a, exp)
        exp *= 10

array=[0]*15
randomnumber(array)
print("Arreglo Original: ")
printarray(array)
radix_sort(array)
print("\nArray Ordenado:")
printarray(array)