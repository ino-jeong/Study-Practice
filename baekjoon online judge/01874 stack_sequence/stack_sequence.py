
    def push(self, x):
        self.data.append(x)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.data.pop()

    def peek(self):
        return self.data[self.size - 1]


n = int(input())
seq = []

for i in range(n):
    seq.append(int(input()))

stack = Stack()
cur_input = 1
commend = []

for i in range(seq[0]):
    stack.push(cur_input)
    commend.append('+')
    cur_input += 1
stack.pop()
commend.append('-')

for element in seq[1:]:
    if element > (cur_input - 1):
        for i in range(element - cur_input + 1):
            stack.push(cur_input)
            commend.append('+')
            cur_input += 1
        stack.pop()
        commend.append('-')
    elif element == stack.peek():
        stack.pop()
        commend.append('-')
    else:
        commend = []
        commend.append('NO')
        break

for com in commend:
    print(com)
