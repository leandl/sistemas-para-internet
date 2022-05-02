from unordered_vector import UnorderedVector
from ordered_vector import OrderedVector

my_list = OrderedVector(10)

my_list.insert(3)
my_list.insert(8)
my_list.insert(5)
my_list.insert(4)
my_list.insert(1)
my_list.insert(9)
my_list.insert(7)
my_list.insert(2)
my_list.insert(13)
my_list.insert(10)


print(my_list)

my_list.remove(2)
print(my_list)

my_list.remove(13)
print(my_list)

my_list.remove(3)
print(my_list)

my_list.insert(15)
print(my_list)

my_list.insert(2)
print(my_list)

my_list.remove(1)
print(my_list)