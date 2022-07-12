import numpy as np
from utils import debug, timer

from ordered_vector import OrderedVector

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort

@timer
@debug
def create_ordered_vector(array):
  ordered_vector = OrderedVector(5000)

  for element in array:
    ordered_vector.insert(element)

@timer
@debug
def sort(type_algorithm, array):
  algorithms = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort
  }

  algorithm_sort = algorithms.get(type_algorithm, None)
  if not algorithm_sort:
    raise Exception("Type Algorithm Not Found")

  return algorithm_sort(array)


array_random = np.random.random_integers(1, high=1000, size=5000)

create_ordered_vector(np.array(array_random))

sort("bubble", np.array(array_random))
sort("selection", np.array(array_random))
sort("insertion", np.array(array_random))


