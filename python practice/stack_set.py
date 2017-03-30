class StackSet():

    def __init__(self):
        self.data_size = 0
        self.stack_size = 3

        self.stack_set = []
        self.stack_idx = -1

    def push(self, value):
        if self.stack_idx == -1:
            self.stack_set.append([])
            self.stack_idx += 1
        elif (self.data_size) % self.stack_size == 0:
            self.stack_set.append([])
            self.stack_idx += 1

        self.stack_set[self.stack_idx].append(value)
        self.data_size += 1

    def pop(self):
        if self.is_empty():
            print('no elements anymore... return None')
            return None

        output = self.stack_set[self.stack_idx].pop()
        self.data_size -= 1

        if self.data_size == (self.stack_size * self.stack_idx):
            del self.stack_set[self.stack_idx]
            self.stack_idx -= 1

        return output

    def is_empty(self):
        if self.data_size == 0:
            return  True
        else:
            return False

    def show_data(self):
        for i in range(len(self.stack_set)):
            print(self.stack_set[i])
        print('stack index :', self.stack_idx)
        print('data size :', self.data_size)


# implementation test
print('* create stack set instance')
ss = StackSet()
ss.show_data()

print('\n* push some data : [1, 2, 3]')
for i in [1, 2, 3]:
    ss.push(i)
ss.show_data()

print('\n* push some more data : [4, 5, 6, 7, 8, 9 ,10]')
for i in [4, 5, 6, 7, 8, 9, 10]:
    ss.push(i)
ss.show_data()

print('\n* pop 1 :', ss.pop())
ss.show_data()

print('\n* pop 2 :', ss.pop())
print('* pop 3 :', ss.pop())
print('* pop 4 :', ss.pop())
print('* pop 5 :', ss.pop())
print('* pop 6 :', ss.pop())
ss.show_data()

print('\n* pop 7 :', ss.pop())
print('n* pop 8 :', ss.pop())
print('n* pop 9 :', ss.pop())
print('n* pop 10 :', ss.pop())
ss.show_data()

print('\n* push again : [0, -9, 24, 0, 11]')
for i in [0, -9, 24, 0, 11]:
    ss.push(i)
ss.show_data()
