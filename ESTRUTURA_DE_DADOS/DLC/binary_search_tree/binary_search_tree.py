# import json
from node import Node


class BinarySearchTree:

    def __init__(self):
        self.__root = None


    def add(self, new_value):
        new_node = Node(new_value)
        if not self.__root:
            self.__root = new_node
            return

        current_node = self.__root

        while current_node:
            if current_node.value == new_value:
                return

            if current_node.value > new_value:
                if current_node.left:
                    current_node = current_node.left
                    continue

                current_node.left = new_node
                return
            
            
            if current_node.right:
                current_node = current_node.right
                continue


            current_node.right = new_node
            return

    def search(self, value):
        current_node = self.__root
        while current_node:
            if current_node.value == value:
                return current_node

            if current_node.value > value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None



    def __str__(self) -> str:
        if not self.__root:
            return ""

        

        return self.__show_graph(self.__root)
            
        # return json.dumps(self.__root.values(), indent=4)


    def __show_graph(self, current_node):
        str_graph = ""

        if current_node.left:
            left_value = current_node.left.value
            str_sub_graph = self.__show_graph(current_node.left)
            str_graph += f"{current_node.value} -> {left_value}" + "\n" + str_sub_graph + "\n"

        if current_node.right:
            right_value = current_node.right.value
            str_sub_graph = self.__show_graph(current_node.right)
            str_graph += f"{current_node.value} -> {right_value}" + "\n" + str_sub_graph + "\n"


        return str_graph
