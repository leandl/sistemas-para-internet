from queue import Queue
from priority_queue import PriorityQueue

my_queue = Queue(10)

my_queue.push(10)
my_queue.push(1)
my_queue.push(13)
my_queue.push(5)

print(my_queue)

my_queue.push(19)
my_queue.push(31)
my_queue.push(14)
my_queue.push(11)
my_queue.push(80)
my_queue.push(18)

print(my_queue)

my_queue.pop()
my_queue.pop()

print(my_queue)

my_queue.push(999)
my_queue.push(9)

print(my_queue)


my_priority_queue = PriorityQueue(10)

my_priority_queue.push(10)
my_priority_queue.push(14)
my_priority_queue.push(31)
my_priority_queue.push(1)
my_priority_queue.push(13)
my_priority_queue.push(5)
my_priority_queue.push(19)
my_priority_queue.push(11)
my_priority_queue.push(80)
my_priority_queue.push(18)

print(my_priority_queue)

print(my_priority_queue.pop())
print(my_priority_queue.pop())
print(my_priority_queue.pop())
print(my_priority_queue.pop())
print(my_priority_queue.pop())

print(my_priority_queue)
