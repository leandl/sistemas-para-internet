import numpy as np

def selection_sort(array):
  print(array)
  for index_main in range(0, len(array) - 1):
    index_minor_element = index_main
    for index_secondary in range(index_main  + 1, len(array)):
      if array[index_minor_element] > array[index_secondary]:
        index_minor_element = index_secondary

    aux = array[index_main]
    array[index_main] = array[index_minor_element]
    array[index_minor_element] = aux
    print(array)
  
  return array


selection_sort(np.array([1, 2, 3, 15, 0]))