import random
def randomnumber(a):
    for i in range(len(a)):
     a[i]=random.randint(1,100)
def printarray(a):
   for i in range(len(a)):
     print(a[i], end=" ")

def SelectionSort(a):
   for i in range(len(a)):
      small=i
      for j in range(i+1,len(a)):
         if a[j]<a[small]:
            small=j
      a[i],a[small]=a[small],a[i]
   
array=[0]*15
randomnumber(array)
print("Arreglo Original: ")
printarray(array)
SelectionSort(array)
print("\nArray Ordenado:")
printarray(array)