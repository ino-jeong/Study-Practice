# queue implementation practice

class Queue(object):

    def __init__(self):
        self.data=[]

    def is_empty(self):
        if len(self.data)<=0:
            return True
        else:
            return False

    def checkSize(self):
        return len(self.data)

    def enQ(self,x):
        self.data.insert(0,x) # use first side of list as rear of queue

    def deQ(self):
        if self.is_empty():
            print("queue is empty")
            return -9999
        else:
            return self.data.pop() # use end side of list as front of queue

    def checkWhole(self):
        print(self.data)

    def front(self):
        if self.is_empty():
            print("queue is empty")
            return -9999
        else:
            return self.data[len(self.data)-1]


# queue implementation test
testQ = Queue()

print("queue is empty now? : ",testQ.is_empty())
print('')

print('enqueue 3 now : ')
testQ.enQ(3)
testQ.checkWhole()
print('check size : ',testQ.checkSize())
print('front value : ',testQ.front())
print('')

print('enqueue 5,-9,0,9,-9,57')
for i in [5,-9,0,9,-9,57]:
    testQ.enQ(i)
testQ.checkWhole()
print('check size : ',testQ.checkSize())
print('front value : ',testQ.front())
print('')

print('dequeue : ',testQ.deQ())
testQ.checkWhole()
print('check size : ',testQ.checkSize())
print('front value : ',testQ.front())
print('')

print('dequeue : ',testQ.deQ())
print('dequeue : ',testQ.deQ())
print('dequeue : ',testQ.deQ())
print('dequeue : ',testQ.deQ())
print('dequeue : ',testQ.deQ())
testQ.checkWhole()
print('check size : ',testQ.checkSize())
print('front value : ',testQ.front())
print('')

print('dequeue : ',testQ.deQ())
testQ.checkWhole()
print('check size : ',testQ.checkSize())
print('front value : ',testQ.front())
print('')

print('dequeue : ',testQ.deQ())
print('check size : ',testQ.checkSize())
print('')

print('enqueue 2,8,7,0,-5')
for i in [2,8,7,0,-5]:
    testQ.enQ(i)
testQ.checkWhole()
print('check size : ',testQ.checkSize())
print('front value : ',testQ.front())

