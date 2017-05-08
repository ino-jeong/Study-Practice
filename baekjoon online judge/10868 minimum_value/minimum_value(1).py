import math

def init(tree_arr, value_map, index, range_start, range_end):
    if range_start == range_end:
        tree_arr[index] = value_map[range_start]

    else:
        mid = (range_start + range_end)//2
        init(tree_arr, value_map, 2 * index, range_start, mid)
        init(tree_arr, value_map, 2 * index + 1, mid + 1, range_end)
        tree_arr[index] = min(tree_arr[2 * index], tree_arr[2 * index + 1])


def query(tree_arr, index, range_start, range_end, i, j):
    if i > range_end or j < range_start:
        return -1
    if i <= range_start and range_end <= j:
        return tree_arr[index]

    mid = (range_start + range_end)//2
    m1 = query(tree_arr, 2 * index, range_start, mid, i, j)
    m2 = query(tree_arr, 2 * index + 1, mid + 1, range_end, i, j)

    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    else:
        return min(m1, m2)


nm = input().split()
n = int(nm[0])
m = int(nm[1])

value_map = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    value_map[i] = int(input())

h = int(math.ceil(math.log2(n)))
tree_arr = [0] * (1 << (h + 1))

init(tree_arr, value_map, 1, 1, n)

order_query = []
for k in range(m):
    line_input = input().split()
    i = int(line_input[0])
    j = int(line_input[1])
    order_query.append((i, j))

for (i, j) in order_query:
    print(query(tree_arr, 1, 1, n, i, j))
