import numpy as np

class QueueException(Exception):
  pass

class Queue:

  def __init__(self, max_elements: int) -> None:
    if max_elements < 0:
      raise QueueException("Minimum value of elements in invalid Queue")

    self.elements = np.array([None] * max_elements)

    self.max_elements = max_elements
    self.queue_length = 0

    self.index_last_element = -1
    self.index_first_element = 0

  def full(self): 
    return self.max_elements == self.queue_length

  def empty(self):
    return self.queue_length == 0

  def __get_next_index(self, current_index: int):
    next_index = current_index + 1
    if next_index == self.max_elements:
      return 0
    
    return next_index

  def push(self, new_value: int) -> None:
    if self.full():
      raise QueueException("Maximum elements in Queue")
    
    self.index_last_element = self.__get_next_index(self.index_last_element)
    self.elements[self.index_last_element] = new_value
    self.queue_length += 1

  def pop(self):
    if self.empty():
      return None

    item = self.elements[self.index_first_element]
    self.elements[self.index_first_element] = None
    self.queue_length -= 1

    self.index_first_element = self.__get_next_index(self.index_first_element)

    return item


  def __str__(self) -> str:
    list_with_element_in_order = []

    index_first_element = self.index_first_element
    number_elements = 0
    

    while number_elements != self.max_elements:
      element = self.elements[index_first_element]
      if element:
        list_with_element_in_order.append(str(element))

      index_first_element = self.__get_next_index(index_first_element)
      number_elements += 1
    

    str_list = " ".join(list_with_element_in_order)
    return f"[ {str_list} ]"