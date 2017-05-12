import math


def init(tree, node, start, end):
    if start == end:
        tree[node] = 1
        return

    mid = (start + end) // 2
    init(tree, 2 * node, start, mid)
    init(tree, 2 * node + 1, mid + 1, end)
    tree[node] = tree[2 * node] + tree[2 * node + 1]


def update(tree, node, start, end, target_idx, value):
    if target_idx > end or target_idx < start:
        return

    if start == end:
        tree[node] += value
        return

    mid = (start + end) // 2
    update(tree, 2 * node, start, mid, target_idx, value)
    update(tree, 2 * node + 1, mid + 1, end, target_idx, value)
    tree[node] = tree[2 * node] + tree[2 * node + 1]


def kth(tree, node, start, end, k):
    if start == end:
        return start

    mid = (start + end) // 2
    if k <= tree[2 * node]:
        return kth(tree, 2 * node, start, mid, k)
    else:
        return kth(tree, 2 * node + 1, mid + 1, end, k - tree[2 * node])


n = int(input())
a = [0]
h = math.ceil(math.log2(n))
tree = [0] * (1 << (h + 1))
init(tree, 1, 1, n)

for i in range(n):
    a.append(int(input()))

ans = [0] * (n + 1)

for i in range(1, n + 1):
    k = a[i] + 1
    position = kth(tree, 1, 1, n, k)
    ans[position] = i
    update(tree, 1, 1, n, position, -1)


for num in ans[1:]:
    print(num)
