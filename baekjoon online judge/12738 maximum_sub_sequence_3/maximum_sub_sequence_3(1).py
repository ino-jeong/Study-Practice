import math


def maximum(tree, node, start, end, i, j):
    if end < i or j < start:
        return 0

    if i <= start and end <= j:
        return tree[node]

    mid = (start + end) // 2
    m1 = maximum(tree, 2 * node, start, mid, i, j)
    m2 = maximum(tree, 2 * node + 1, mid + 1, end, i, j)

    return max(m1, m2)


def update(tree, node, start, end, target_idx, value):
    if end < target_idx or target_idx < start:
        return

    tree[node] = max(tree[node], value)

    if start != end:
        mid = (start + end) // 2
        update(tree, 2 * node, start, mid, target_idx, value)
        update(tree, 2 * node + 1, mid + 1, end, target_idx, value)
    return


n = int(input())
line_input = input().split()
line_input.sort()

a = [0]

cur = int(line_input[0])
a.append(1)
last_num = 1
last_idx = 1

for numb in line_input[1:]:
    num = int(numb)

    if cur == num:
        a.append(last_num)
        last_idx += 1
    else:
        cur = num
        last_num += 1
        last_idx += 1
        a.append(last_num)

h = math.ceil(math.log2(n))
tree = [0] * (1 << (h + 1))

ans = 0
for num in a:
    prev_max = maximum(tree, 1, 1, n, 1, num - 1)
    now_max = prev_max + 1
    update(tree, 1, 1, n, num, now_max)

    ans = max(ans, now_max)

print(ans)
