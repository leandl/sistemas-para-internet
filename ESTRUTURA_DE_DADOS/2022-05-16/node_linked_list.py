class NodeLinkedList:
    def __init__(self, value: int):
        self.__value = value
        self.__next = None

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    def __str__(self):
        if not self.__next:
            return str(self.__value)

        return f"{self.__value}, {self.__next}"
