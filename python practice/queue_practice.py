# queue implementation practice

from queue import Queue


class Queue(object):

    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) <= 0:
            return True
        else:
            return False

    def check_size(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.insert(0, value)  # use first side of list as rear of queue

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return None
        else:
            return self.data.pop()  # use end side of list as front of queue

    def print_queue(self):
        print(self.data)

    def front(self):
        if self.is_empty():
            print("queue is empty")
            return None
        else:
            return self.data[len(self.data)-1]


# queue implementation test
# uncomment each line to test
#
test_queue = Queue()
#
# print("queue is empty now? : ",test_queue.is_empty())
# print('')
#
# print('enqueue 3 now : ')
# test_queue.enqueue(3)
# test_queue.print_queue()
# print('check size : ', test_queue.check_size())
# print('front value : ', test_queue.front())
# print('')
#
# print('enqueue 5,-9,0,9,-9,57')
# for i in [5, -9, 0, 9, -9, 57]:
#     test_queue.enqueue(i)
# test_queue.print_queue()
# print('check size : ', test_queue.check_size())
# print('front value : ', test_queue.front())
# print('')
#
# print('dequeue : ', test_queue.dequeue())
# test_queue.print_queue()
# print('check size : ', test_queue.check_size())
# print('front value : ', test_queue.front())
# print('')
#
# print('dequeue : ', test_queue.dequeue())
# print('dequeue : ', test_queue.dequeue())
# print('dequeue : ', test_queue.dequeue())
# print('dequeue : ', test_queue.dequeue())
# print('dequeue : ', test_queue.dequeue())
# test_queue.print_queue()
# print('check size : ', test_queue.check_size())
# print('front value : ', test_queue.front())
# print('')
#
# print('dequeue : ', test_queue.dequeue())
# test_queue.print_queue()
# print('check size : ', test_queue.check_size())
# print('front value : ', test_queue.front())
# print('')
#
# print('dequeue : ', test_queue.dequeue())
# print('check size : ', test_queue.check_size())
# print('')
#
# print('enqueue 2,8,7,0,-5')
# for i in [2, 8, 7, 0, -5]:
#     test_queue.enqueue(i)
# test_queue.print_queue()
# print('check size : ', test_queue.check_size())
# print('front value : ', test_queue.front())
#
#
# for i in range(100000):
#     test_queue.enqueue(i)

q = Queue()

for i in range(100000):
    q.enqueue(i)

