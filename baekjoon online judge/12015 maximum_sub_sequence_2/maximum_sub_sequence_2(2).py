import math
from sys import stdin
max_val = 1000000


def maximum(tree, node, start, end, i, j):
    if end < i or j < start:
        return 0

    if i <= start and end <= j:
        return tree[node]

    # if [i, j] range is over [start, end] range

    mid = (start + end) // 2
    # 1. left
    m1 = maximum(tree, 2 * node, start, mid, i, j)

    # 2. right
    m2 = maximum(tree, 2 * node + 1, mid + 1, end, i, j)
    return max(m1, m2)


def update(tree, node, start, end, target_idx, value):
    if end < target_idx or target_idx < start:
        return

    tree[node] = max(tree[node], value)
    if start != end:
        mid = (start + end) // 2
        # 1. left
        update(tree, 2 * node, start, mid, target_idx, value)
        # 2. right
        update(tree, 2 * node + 1, mid + 1, end, target_idx, value)


    return


# n = int(input())
n = int(stdin.readline())

h = math.ceil(math.log2(max_val))
tree = [0] * (1 << (h + 1))

ans = 0

# line_input = input().split()
line_input = stdin.readline().split()
for numb in line_input:
    num = int(numb)
    prev_max = maximum(tree, 1, 1, max_val, 1, num - 1)
    now_max = prev_max + 1
    update(tree, 1, 1, max_val, num, now_max)

    ans = max(ans, now_max)

print(ans)

