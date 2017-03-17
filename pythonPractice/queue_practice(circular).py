# queue implementation practice


class CircularQueue(object):

    def __init__(self):
        self.capacity = 5  # initial length of data array.

        # initializing data array
        self.data = []
        for i in range(self.capacity):
            self.data.append(None)

        self.front = 0
        self.end = -1
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size == self.capacity:
            return True
        else:
            return False

    def check_size(self):
        return self.size

    def check_capacity(self):
        return self.capacity

    def print_queue(self):
        print(self.data)
        print('front :', self.front, '/ end :', self.end)

    def front(self):
        if self.is_empty():
            print("queue is empty")
            return None
        else:
            return self.data[self.front]

    # return circular index if input index is larger than maximum index of data array
    def get_circular_index(self, idx):
        if idx >= self.capacity:
            idx %= self.capacity
        return idx

    # reallocate data array as twice larger one
    def data_reallocate(self):
        # initializing new data array
        new_capacity = 2*self.capacity
        self.new_data = []
        for i in range(new_capacity):
            self.new_data.append(None)

        # copy old data into new data array. rearrange data location so front index shall be zero(0)
        j = 0
        while self.front != self.end:
            self.new_data[j] = self.data[self.front]
            j += 1
            self.front += 1
            self.front = self.get_circular_index(self.front)

        self.new_data[j] = self.data[self.end]  # after while loop, final data (at end index) is not copied yet.

        # reset front & end index, its capacity and data array name
        self.front = 0
        self.end = j
        self.data = self.new_data
        self.capacity = new_capacity

    def enqueue(self, value):
        if self.is_full():
            self.data_reallocate()

        self.size += 1
        self.end += 1
        self.end = self.get_circular_index(self.end)  # if increased index is out of maximum, get circular index

        self.data[self.end] = value

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return None
        else:
            front_data = self.data[self.front]  # copy data which shall be popped.
            self.data[self.front] = None  # remove popped data to prevent confusion
            self.front += 1
            self.size -= 1
            self.front = self.get_circular_index(self.front)  # if increased index is out of maximum, get circular index
            return front_data  # return copied data


# Circular array queue implementation test
# uncommend each line to test
# cq = CircularQueue()
# print('create Circular Queue instance. check size & capacity : ', cq.check_size(), '&', cq.check_capacity())
# print('is queue empty? :', cq.is_empty())
# print('\nenqueue some data : [5,6,8,10,9]')
# for i in [5, 6, 8, 10, 9]:
#     cq.enqueue(i)
# print('is queue full now? :', cq.is_full())
# cq.print_queue()
#
# print('\ndequeue some 3 data now')
# print('dequeue :', cq.dequeue())
# print('dequeue :', cq.dequeue())
# print('dequeue :', cq.dequeue())
# print('check size & capacity :', cq.check_size(), '&', cq.check_capacity())
# cq.print_queue()
#
# print('\nenqueue again now : [7,-2,-7]')
# for i in [7, -2, -7]:
#     cq.enqueue(i)
# print('check size & capacity :', cq.check_size(), '&', cq.check_capacity())
# cq.print_queue()
#
# print('\nenqueue more. test array reallocation : [12,15,19]')
# for i in [12, 15, 19]:
#     cq.enqueue(i)
# print('check size & capacity :', cq.check_size(), '&', cq.check_capacity())
# cq.print_queue()
# cq.check_front_end_index()
