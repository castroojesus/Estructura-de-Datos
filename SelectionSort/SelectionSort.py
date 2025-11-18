def SelectionSort(a):
   for i in range(len(a)):
      small=i
      for j in range(i+1,len(a)):
         if a[small]<a[j]:
            small=j
      a[i],a[small]=a[small],a[i]
def printarray(a):
   for i in range(len(a)):
     print(a[i], end=" ")   
array=[16,45,0,45,78,2,1,9,5 ]

print("Arreglo Original: ")
printarray(array)
SelectionSort(array)
print("\nArray Ordenado:")
printarray(array)