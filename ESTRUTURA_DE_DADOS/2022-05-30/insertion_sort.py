import numpy as np

def selection_sort(array):
  for i in range(1, len(array)):
    item = array[i]
    print(array)
    for j in range(i-1, -1, -1):
      if item < array[j]:
        array[j] = item
        break
      
      array[j + 1] = array[j] 
  
  return array


selection_sort(np.array([1, 2, 3, 15, 0]))