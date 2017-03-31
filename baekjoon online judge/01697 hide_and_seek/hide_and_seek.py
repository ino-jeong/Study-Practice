# class Queue():
#     def __init__(self):
#         self.position = []
#         self.time = []
#
#     def put(self, pos, t):
#         self.position.append(pos)
#         self.time.append(t)
#
#     def get(self):
#         return (self.position.pop(0), self.time.pop(0))
#
#
import queue


def hide_and_seek(n, k):
    # data_queue = Queue()

    if n == k:
        return 0

    data_queue = queue.Queue()
    visit_hash = {}

    cur = n
    cur_time = 0
    data_queue.put((cur, cur_time))

    while cur != k:
        cur, cur_time = data_queue.get()
        if cur not in visit_hash and (0 <= cur <= 100000):
            visit_hash[cur] = cur_time

            if 2 * cur <= 100000 and (not (2 * cur) in visit_hash):
                data_queue.put((2 * cur, cur_time + 1))

            if cur + 1 <= 100000 and (not (cur + 1) in visit_hash):
                data_queue.put((cur + 1, cur_time + 1))

            if cur - 1 >= 0 and (not (cur - 1) in visit_hash):
                data_queue.put((cur - 1, cur_time + 1))

    return visit_hash[k]


line_input = input()
line_input = line_input.split(' ')

n = int(line_input[0])
k = int(line_input[1])

print(hide_and_seek(n,k))
