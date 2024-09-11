import pdb
def selectionSort(arr):
   n = len(arr)
   for i in range(n):
       lowestIndex = i
       for j in range(n):
           if arr[j] < arr[lowestIndex]:
               lowestIndex = j


       breakpoint()
       lowestNum = arr[lowestIndex]
       arr[lowestIndex] = arr[i]
       arr[i] = lowestNum


       n = n - 1


   return arr