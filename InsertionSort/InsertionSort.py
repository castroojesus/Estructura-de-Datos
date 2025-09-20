import random
def randomnumber(a):
    for i in range(len(a)):
     a[i]=random.randint(1,100)
def printarray(a):
   for i in range(len(a)):
     print(a[i], end=" ")
def InsertionSort(a):
   for i in range(1,len(a)):
      temp=a[i]
      j=i-1
      while j>=0 and temp<a[j]:
         a[j+1]=a[j]
         j=j-1
      a[j+1]=temp

array=[0]*15
randomnumber(array)
print("Arreglo Original: ")
printarray(array)
InsertionSort(array)
print("\nArray Ordenado:")
printarray(array)
    