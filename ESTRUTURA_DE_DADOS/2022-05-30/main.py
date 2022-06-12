import numpy as np
from utils import debug

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

@debug
def sort(array, type_algorithm = "bubble"):
  algorithms = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort
  }

  algorithm_sort = algorithms.get(type_algorithm, None)
  if not algorithm_sort:
    raise Exception("Type Algorithm Not Found")

  return algorithm_sort(array)


sort(np.array([8, 6, 9, 2, 10, 1]), "bubble")
sort(np.array([1, 2, 3, 15, 0, 6]), "selection")
sort(np.array([8, 6, 9, 2, 10, 1]), "insertion")