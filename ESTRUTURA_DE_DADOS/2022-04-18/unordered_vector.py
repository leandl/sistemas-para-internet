import numpy as np

class UnorderedVectorException(Exception):
    pass

class UnorderedVector:

    def __init__(self, max_elements: int) -> None:
        if max_elements < 0:
            raise UnorderedVectorException(
                "Minimum value of elements in invalid UnorderedVector"
            )

        self.elements = np.array([None] * max_elements)
        self.max_elements = max_elements
        self.index_last_element = -1

    def insert(self, new_value: int) -> None:
        new_index_last_element = self.index_last_element + 1

        if new_index_last_element == self.max_elements:
            raise UnorderedVectorException("Maximum elements in UnorderedVector")

        self.elements[new_index_last_element] = new_value
        self.index_last_element = new_index_last_element

    def get_index_last_element(self) -> int:
        return self.index_last_element

    def __str__(self) -> str:
        str_list = " ".join([ 
            str(x) for x in self.elements if not x == None 
        ])

        return f"[ {str_list} ]"