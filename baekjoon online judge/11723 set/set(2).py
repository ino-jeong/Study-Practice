import sys

class Set():
    def __init__(self):
        self.s = 0

    def add(self, x):
        if not self.check(x):
            self.s = self.s | (1 << x)

    def remove(self, x):
        if self.check(x):
            self.s = self.s & ~(1 << x)

    def check(self, x):
        if self.s & (1 << x):
            return 1
        else:
            return 0

    def toggle(self, x):
        self.s = self.s ^ (1 << x)

    def all(self):
        self.s = int(1 << 21) - 1

    def empty(self):
        self.s = 0

test_set = Set()
cases = int(sys.stdin.readline())
string_buffer = []

for c in range(cases):
    line_input = sys.stdin.readline()
    line_input = line_input.strip('\n').split(' ')

    if line_input[0] == 'all':
        test_set.all()

    elif line_input[0] == 'empty':
        test_set.empty()

    elif line_input[0] == 'add':
        input_num = int(line_input[1])
        test_set.add(input_num)

    elif line_input[0] == 'remove':
        input_num = int(line_input[1])
        test_set.remove(input_num)

    elif line_input[0] == 'check':
        input_num = int(line_input[1])
        string_buffer.append(test_set.check(input_num))

    elif line_input[0] == 'toggle':
        input_num = int(line_input[1])
        test_set.toggle(input_num)

    else:
        continue

for s in string_buffer:
    print(s)
