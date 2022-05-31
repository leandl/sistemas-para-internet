import numpy as np

def bubble_sort(_array):
  last_index = len(_array) - 1
  
  while 0 != last_index:
    print(_array)
    index = 0
    while index < last_index:

      if _array[index] > _array[index + 1]:
        aux = _array[index]
        _array[index] = _array[index + 1]
        _array[index + 1] = aux

      
      index +=1
    last_index -= 1
    
  print(_array)
  return _array
    

bubble_sort(np.array([8, 6, 9, 2, 10, 1]))