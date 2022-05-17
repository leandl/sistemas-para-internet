from linked_list import LinkedList

my_list = LinkedList()

my_list.add(3)
my_list.add(4)

my_list.add(5)
my_list.add(2)

my_list.add(9)
my_list.add(1)

my_list.add(8)

my_list.add_first(50)



print(my_list)

my_list.remove(10)
my_list.remove(3)
my_list.remove(50)
print(my_list)

for a in my_list:
    print(a)


print("len", len(my_list))