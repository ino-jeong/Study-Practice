class Queue():
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
            return self.data.pop(0)

    def size(self):
        return self.data_size

    def empty(self):
        if self.data_size <= 0:
            return 1
        else:
            return 0

    def front(self):
        if self.data_size <= 0:
            return -1
        else:
            return self.data[0]

    def back(self):
        if self.data_size <= 0:
            return -1
        else:
            return self.data[len(self.data)-1]


n = int(input())
result = []

queue = Queue()

for i in range(n):
    input_line = input()
    line = input_line.split()

    if line[0] == 'push':
        queue.push(int(line[1]))
    elif line[0] == 'pop':
        result.append(queue.pop())
    elif line[0] == 'size':
        result.append(queue.size())
    elif line[0] == 'empty':
        result.append(queue.empty())
    elif line[0] == 'front':
        result.append(queue.front())
    elif line[0] == 'back':
        result.append(queue.back())

for output in result:
    print(output)
