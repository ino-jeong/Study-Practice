class Deque(object):
    def __init__(self):
        self.data = []

    def push_front(self, x):
        self.data.insert(0, x)

    def push_back(self, x):
        self.data.append(x)

    def pop_front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.data.pop(0)

    def pop_back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.data.pop()

    def size(self):
        return len(self.data)

    def empty(self):
        if len(self.data) > 0:
            return 0
        else:
            return 1

    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.data[0]

    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.data[len(self.data) - 1]

cases = int(input())
dq = Deque()

for c in range(cases):
    line_input = input()
    line_input = line_input.split(' ')

    if line_input[0] == 'push_front':
        x = int(line_input[1])
        dq.push_front(x)

    elif line_input[0] == 'push_back':
        x = int(line_input[1])
        dq.push_back(x)

    elif line_input[0] == 'pop_front':
        print(dq.pop_front())

    elif line_input[0] == 'pop_back':
        print(dq.pop_back())

    elif line_input[0] == 'size':
        print(dq.size())

    elif line_input[0] == 'empty':
        print(dq.empty())

    elif line_input[0] == 'front':
        print(dq.front())

    elif line_input[0] == 'back':
        print(dq.back())

    else:
        continue

