class NodeDoubleLinkedList:
  def __init__(self, value: int):
    self.__value = value
    self.__prev = None
    self.__next = None

  def get_value(self):
    return self.__value

  def get_next(self):
    return self.__next

  def set_next(self, node):
    self.__next = node

  def get_prev(self):
    return self.__prev

  def set_prev(self, node):
    self.__prev = node

  def __str__(self):
    return str(self.__value)
    # return str({
    #   "value": self.__value,
    #   "prev": self.__prev.__str__(),
    #   "next": self.__next
    # })