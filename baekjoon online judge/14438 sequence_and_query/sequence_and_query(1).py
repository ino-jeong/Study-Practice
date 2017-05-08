import math

def init(tree_arr, value_map, node, start, end):
    if start == end:
        tree_arr[node] = value_map[start]
    else:
        mid = (start + end) // 2
        init(tree_arr, value_map, node * 2, start, mid)
        init(tree_arr, value_map, node * 2 + 1, mid + 1, end)
        tree_arr[node] = min(tree_arr[node * 2], tree_arr[node * 2 + 1])


def query(tree_arr, value_map, node, start, end, i, j):
    if end < i or start > j:
        return -1
    if i <= start and end <= j:
        return tree_arr[node]

    mid = (start + end)//2
    left_min = query(tree_arr, value_map, 2 * node, start, mid, i, j)
    right_min = query(tree_arr, value_map, 2 * node + 1, mid + 1, end, i, j)

    if left_min == -1:
        return right_min
    elif right_min == -1:
        return left_min
    else:
        return min(left_min, right_min)


def update(tree_arr, node, start, end, target, value):
    if target < start or target > end:
        return

    if start == end:
        tree_arr[node] = value
        return

    mid = (start + end) // 2
    update(tree_arr, 2 * node, start, mid, target, value)
    update(tree_arr, 2 * node + 1, mid + 1, end, target, value)
    tree_arr[node] = min(tree_arr[2 * node], tree_arr[2 * node + 1])
    return


n = int(input())

line_input = input().split()
value_map = [0] * (n + 1)
for i in range(1, n + 1):
    num = int(line_input[i - 1])
    value_map[i] = num

h = int(math.ceil(math.log2(n)))
tree_arr = [0] * (1 << (h + 1))

init(tree_arr, value_map, 1, 1, n)

m = int(input())
order_query = []
for i in range(m):
    line_input = input().split()
    a, b, c = int(line_input[0]), int(line_input[1]), int(line_input[2])
    order_query.append((a, b, c))

for (a, b, c) in order_query:
    if a == 1:
        update(tree_arr, 1, 1, n, b, c)
    else:
        print(query(tree_arr, value_map, 1, 1, n, b, c))

