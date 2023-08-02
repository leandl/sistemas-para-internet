from binary_search_tree import BinarySearchTree


b = BinarySearchTree()

b.add(17)
b.add(13)
b.add(31)
b.add(22)
b.add(14)
b.add(36)
b.add(242)
b.add(1)
b.add(19)
b.add(20)


print(b.search(13).values())
