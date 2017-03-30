# stack implementation practice

class Stack(object):

    def __init__(self):
        self.size=0
        self.data = []

    def push(self,x):
        self.data.append(x)
        self.size=self.size+1

    def pop(self):
        if(self.is_empty()):
            print("the stack is empty")
        else:
            self.size = self.size - 1
            if (self.size <= 0):
                print("no data any more after this value")
            return self.data.pop()


    def checkSize(self):
        return self.size

    def is_empty(self):
        if(self.size<=0):
            return True
        else:
            return False

    def peek(self):
        if(self.is_empty()):
            print('the stack is empty')
            return -9999
        else:
            return self.data[self.size-1]

    def checkWhole(self):
        if (self.is_empty()):
            print('the stack is empty')
        else:
            print(self.data)

# implementation test
testStack = Stack()

print("the stack is empty now? : ",testStack.is_empty())
print("check size : ",testStack.checkSize())

print("push 7 now")
testStack.push(7)
print ("")

print("the stack is empty now? : ",testStack.is_empty())
print("peek value : ",testStack.peek())
print("check size : ",testStack.checkSize())
testStack.checkWhole()
print ("")

print("push 8,4,12,-7,0,55")
for i in [8,4,12,-7,0,55]:
    testStack.push(i)
print("check peek value : ",testStack.peek())
print("check size : ",testStack.checkSize())
testStack.checkWhole()
print ("")

print("pop : ",testStack.pop())
print("check peek value : ",testStack.peek())
print("check size : ",testStack.checkSize())
testStack.checkWhole()
print ("")

print("pop : ",testStack.pop())
print("pop : ",testStack.pop())
print("pop : ",testStack.pop())
print("check peek value : ",testStack.peek())
print("check size : ",testStack.checkSize())
testStack.checkWhole()
print ("")

print("pop : ",testStack.pop())
print("pop : ",testStack.pop())
print("pop : ",testStack.pop())
print("check size : ",testStack.checkSize())
testStack.checkWhole()
print ("")

print("pop : ",testStack.pop())
print("check size : ",testStack.checkSize())
testStack.checkWhole()
print ("")

print("push 27,1,-8")
for i in [27,1,-8]:
    testStack.push(i)
print("check peek value : ",testStack.peek())
print("check size : ",testStack.checkSize())
testStack.checkWhole()
print ("")
