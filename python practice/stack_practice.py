# stack implementation practice


class Stack(object):

    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, value):
        self.data.append(value)
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("the stack is empty")
        else:
            self.size -= 1
            if self.size <= 0:
                print("no data any more after this value")
            return self.data.pop()

    def check_size(self):
        return self.size

    def is_empty(self):
        if self.size <= 0:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            print('the stack is empty')
            return None
        else:
            return self.data[self.size-1]

    def print_stack(self):
        if self.is_empty():
            print('the stack is empty')
        else:
            print(self.data)

# implementation test
# uncomment each line to test
#
# test_stack = Stack()
#
# print("the stack is empty now? : ", test_stack.is_empty())
# print("check size : ", test_stack.check_size())
#
# print("push 7 now")
# test_stack.push(7)
# print ("")
#
# print("the stack is empty now? : ", test_stack.is_empty())
# print("peek value : ", test_stack.peek())
# print("check size : ", test_stack.check_size())
# test_stack.print_stack()
# print ("")
#
# print("push 8,4,12,-7,0,55")
# for i in [8, 4, 12, -7, 0, 55]:
#     test_stack.push(i)
# print("check peek value : ", test_stack.peek())
# print("check size : ", test_stack.check_size())
# test_stack.print_stack()
# print ("")
#
# print("pop : ", test_stack.pop())
# print("check peek value : ", test_stack.peek())
# print("check size : ", test_stack.check_size())
# test_stack.print_stack()
# print ("")
#
# print("pop : ", test_stack.pop())
# print("pop : ", test_stack.pop())
# print("pop : ", test_stack.pop())
# print("check peek value : ", test_stack.peek())
# print("check size : ", test_stack.check_size())
# test_stack.print_stack()
# print ("")
#
# print("pop : ", test_stack.pop())
# print("pop : ", test_stack.pop())
# print("pop : ", test_stack.pop())
# print("check size : ", test_stack.check_size())
# test_stack.print_stack()
# print ("")
#
# print("pop : ", test_stack.pop())
# print("check size : ", test_stack.check_size())
# test_stack.print_stack()
# print ("")
#
# print("push 27,1,-8")
# for i in [27, 1, -8]:
#     test_stack.push(i)
# print("check peek value : ", test_stack.peek())
# print("check size : ", test_stack.check_size())
# test_stack.print_stack()
# print ("")
