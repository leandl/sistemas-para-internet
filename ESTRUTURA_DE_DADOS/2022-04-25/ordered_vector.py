import numpy as np

class OrderedVectorException(Exception):
    pass

class OrderedVector:

    def __init__(self, max_elements: int) -> None:
        if max_elements < 0:
            raise OrderedVectorException(
                "Minimum value of elements in invalid OrderedVector"
            )

        self.elements = np.array([None] * max_elements)
        self.max_elements = max_elements
        self.index_last_element = -1

    def insert(self, new_value: int) -> None:
        new_index_last_element = self.index_last_element + 1

        if new_index_last_element == self.max_elements:
            raise OrderedVectorException("Maximum elements in OrderedVector")

        index_frist_more = self.__findFristMore(new_value)
        if index_frist_more == -1 or index_frist_more == new_index_last_element:
            self.elements[new_index_last_element] = new_value
            self.index_last_element = new_index_last_element
            return

        
        for index in range(new_index_last_element, index_frist_more, -1):
            self.elements[index] = self.elements[index - 1]

        self.elements[index_frist_more] = new_value
        self.index_last_element = new_index_last_element
        
    def __findFristMore(self, value: int):
        if self.index_last_element == -1:
            return -1

        for index in range(self.index_last_element + 1):
            if value < self.elements[index]:
                return index
    
        return self.index_last_element + 1
        

    def find(self, value: int):
        if self.index_last_element == -1:
            return -1

        index_max = self.index_last_element + 1
        index_min = 0

        while index_min <= index_max:
            index = (index_min + index_max) // 2
            item = self.elements[index]

            if item == value:
                return index
            elif item < value:
                index_min = index + 1
            else:
                index_max = index - 1

        return -1

    def remove(self, value: int):
        index_item_remove = self.find(value)

        if index_item_remove == -1:
            return -1
            
        for index in range(index_item_remove, self.index_last_element):
            self.elements[index] = self.elements[index + 1]

        self.elements[self.index_last_element] = None
        self.index_last_element -= 1


    def __str__(self) -> str:
        str_list = " ".join([ 
            str(x) for x in self.elements if not x == None 
        ])

        return f"[ {str_list} ]"