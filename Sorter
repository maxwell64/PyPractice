#Sorts an array using either merge sort or bubble sort methods, as chosen by user

def Sort(arr):
  
  method = input('Merge or Bubble? ')

  method = method.lower()

  if method[0] == 'm':

    MergeSort(arr)

    print(arr)

  elif method[0] == 'b':

    BubbleSort(arr)

  else:
    method = input('Not a method, try again: ')
    
def MergeSort(arr):

  if len(arr)>1:

    mid = len(arr)//2

    l = arr[:mid]
    r = arr[mid:]

    MergeSort(l)
    MergeSort(r)

    i = j = k = 0

    while i < len(l) and j < len(r):
      
      if l[i] > r[j]:

        arr[k] = r[j]

        j += 1
      else:

        arr[k] = l[i]

        i += 1
      
      k += 1

def BubbleSort(arr):

  n = len(arr)

  for i in range(n):

    for j in range(0,n-i-1):

      if arr[j] > arr[j+1]:

        arr[j],arr[j+1] = arr[j+1],arr[j]
  
  print(arr)

test = [1,3,4,25,6,16,8,29,64]

Sort(test)
