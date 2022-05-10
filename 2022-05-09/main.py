from queue import Queue

my_queue = Queue(10)

my_queue.push(10)
my_queue.push(1)
my_queue.push(13)
my_queue.push(5)
my_queue.push(19)
my_queue.push(31)
my_queue.push(14)
my_queue.push(11)
my_queue.push(80)
my_queue.push(18)


my_queue.pop()
my_queue.pop()

my_queue.push(999)
my_queue.push(9)



print(my_queue)