import numpy as np

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

def sort(array, type_algorithm = "bubble"):
  algorithms = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort
  }

  if not algorithms.get(type_algorithm, None):
    raise Exception("Type Algorithm Not Found")

  algorithm_sort = algorithms.get(type_algorithm)
  return algorithm_sort(array)


sort(np.array([8, 6, 9, 2, 10, 1]), "bubble")
sort(np.array([1, 2, 3, 15, 0]), "selection")
print(sort(np.array([8, 6, 9, 2, 10, 1]), "insertion"))