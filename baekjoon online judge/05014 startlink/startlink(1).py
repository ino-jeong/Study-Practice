# 미해결 (시간초과)

class Queue():
    def __init__(self):
        self.position = []
        self.time = []

    def put(self, pos, t):
        self.position.append(pos)
        self.time.append(t)

    def get(self):
        return (self.position.pop(0), self.time.pop(0))

    def is_empty(self):
        if len(self.position) > 0:
            return False
        else:
            return True

def find_way(f,s,g,u,d):

    pos = s
    button = 0

    if pos == g:
        return button
    elif u > f or d > f:
        return 'use the stairs'

    visit_hash = {}
    pos_queue = Queue()
    pos_queue.put(pos,button)
    visit_hash[pos] = button

    while pos != g:
        if pos_queue.is_empty() is True:
            break

        pos, button = pos_queue.get()
        if button > abs(g - s):
            break

        if (pos + u) <= f and (pos + u) not in visit_hash:
            pos_queue.put(pos + u, button + 1)
            visit_hash[pos + u] = button + 1

        if (pos - d) >= 0 and (pos - d) not in visit_hash:
            pos_queue.put(pos - d, button + 1)
            visit_hash[pos - d] = button + 1

    if g in visit_hash:
        return visit_hash[g]
    else:
        return 'use the stairs'


line_input = input()
line_input = line_input.split(' ')
line_input = [int(ch) for ch in line_input]

f = line_input[0]
s = line_input[1]
g = line_input[2]
u = line_input[3]
d = line_input[4]

print(find_way(f,s,g,u,d))

#f, s, g, u, d
# test_input = [
#     [10, 1, 10, 2, 1],
#     [100, 2, 1, 1, 0],
#     [10, 1, 10, 1, 0]
# ]
#
# for line_input in test_input:
#     f = line_input[0]
#     s = line_input[1]
#     g = line_input[2]
#     u = line_input[3]
#     d = line_input[4]
#
#     print(find_way(f,s,g,u,d))
