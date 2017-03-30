class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins_stack= []
        self.min_value = None
        self.size = 0

    def push(self, value):
        self.size += 1
        self.stack.append(value)

        if self.min_value is None or value < self.min_value:
            self.min_value = value

        self.mins_stack.append(self.min_value)

    def pop(self):
        if self.is_empty():
            print('stack is empty')
            return None

        self.size -= 1

        self.mins_stack.pop()
        if self.size == 0:
            self.min_value = None
        else:
            last_idx = len(self.mins_stack) - 1
            self.min_value = self.mins_stack[last_idx]

        return self.stack.pop()

    def get_minimum(self):
        return self.min_value

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def show_data(self):
        print('stack array :', self.stack)
        print('min array :', self.mins_stack)
        print('data size :', self.size)


# implementation test
print('* create minimum accessible stack')
ms = MinStack()
ms.show_data()

print('\n* push some data : [4, 7, 3, 2, 8]')
for i in [4, 7, 3, 2, 8]:
    ms.push(i)
ms.show_data()

print('\n* get minimum value :', ms.get_minimum())

print('\n* pop twice')
print('* pop 1 :', ms.pop())
print('* pop 2 :', ms.pop())
ms.show_data()
print('* minimum value is now :', ms.get_minimum())

print('\n pop again')
print('* pop :', ms.pop())
ms.show_data()
print('* minimum value is now :', ms.get_minimum())

print('\n pop again')
print('* pop :', ms.pop())
ms.show_data()
print('* minimum value is now :', ms.get_minimum())

print('\n* try pop again')
print('* pop :', ms.pop())
ms.show_data()
print('* minimum value is now :', ms.get_minimum())

print('\n* push other data : [1, 5, -9, -11, 13, 1, 27]')
for i in [1, 5, -9, -11, 13, 1, 27]:
    ms.push(i)
ms.show_data()
