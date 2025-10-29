import random

def randomnumber(a):
    for i in range(len(a)):
     a[i]=random.randint(1,100)
def printarray(a):
   for i in range(len(a)):
     print(a[i], end=" ")

#Algoritmo de ordenamiento Bucket Sort
def insertion_sort(bucket):
    for j in range(1, len(bucket)):
        val = bucket[j]
        k = j - 1
        while k >= 0 and bucket[k] > val:
            bucket[k + 1] = bucket[k]
            k -= 1
        bucket[k + 1] = val  

def bucket_sort(inputArr):
    s = len(inputArr)
    bucketArr = [[] for _ in range(s)]

    max_val = max(inputArr)

    # Distribuir los elementos en los buckets 
    for j in inputArr:
        normalized = j / (max_val + 1)
        bi = int(s * normalized)
        bucketArr[bi].append(j)

    # Ordenar cada bucket con insertion sort
    for bucket in bucketArr:
        insertion_sort(bucket)

    # Concatenar los buckets ordenados
    idx = 0
    for bucket in bucketArr:
        for j in bucket:
            inputArr[idx] = j
            idx += 1

array=[0]*15
randomnumber(array)
print("Arreglo Original: ")
printarray(array)
bucket_sort(array)
print("\nArray Ordenado:")
printarray(array)