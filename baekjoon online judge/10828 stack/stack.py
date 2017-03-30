class Stack():
    def __init__(self):
        self.data = []
        self.data_size = 0

    def push(self, x):
        self.data.append(x)
        self.data_size += 1

    def pop(self):
        if self.data_size <= 0:
            return -1
        else:
            self.data_size -= 1
            return self.data.pop()

    def size(self):
        return self.data_size

    def empty(self):
        if self.data_size <= 0:
            return 1
        else:
            return 0

    def top(self):
        if self.data_size <= 0:
            return -1
        else:
            return self.data[len(self.data)-1]

stack = Stack()

n = int(input())
for i in range(n):
    line_input = input()
    line_input = line_input.split(' ')

    if line_input[0] == 'push':
        x = int(line_input[1])
        stack.push(x)

    elif line_input[0] == 'pop':
        print(stack.pop())

    elif line_input[0] == 'size':
        print(stack.size())

    elif line_input[0] == 'empty':
        print(stack.empty())

    elif line_input[0] == 'top':
        print(stack.top())
