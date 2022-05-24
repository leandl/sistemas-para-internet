from node_linked_list import NodeLinkedList

class LinkedList:

    def __init__(self):
        self.__length = 0
        self.__head = None
        self.__tail = None

    def empty(self):
        return self.__head == None

    def add(self, new_value: int):
        new_node = NodeLinkedList(new_value)
        self.__length += 1

        if self.empty():
            self.__head = new_node
            self.__tail = new_node
            return
        
        self.__tail.set_next(new_node)
        self.__tail = new_node

    def add_first(self, new_value):
        new_node = NodeLinkedList(new_value)
        self.__length += 1

        if self.empty():
            self.__head = new_node
            self.__tail = new_node
            return

        new_node.set_next(self.__head)
        self.__head = new_node 

    def remove_first(self):
        if not self.__head:
            return

        self.__length -= 1
        new_first = self.__head.get_next()
        self.__head = new_first

    def search(self, value, is_parent = False):
        node = self.__head
        parent = None

        while node:
            if node.get_value() == value:
                if is_parent:
                    return parent, node
                return node

            parent = node
            node = node.get_next()

        if is_parent:
            return None, None

        return None

        
    def remove(self, value):
        parent, child = self.search(value, True)
        
        if parent:
            self.__length -= 1
            parent.set_next(child.get_next())
            return

        if child:
            self.remove_first()
        

    def __iter__(self):
        node = self.__head
        while node:
            yield node.get_value()
            node = node.get_next()

    def __len__(self):
        return self.__length

    def __str__(self):
        str_list = ", ".join([ str(node) for node in self ])
        return f"LinkedList([{str_list}])"
