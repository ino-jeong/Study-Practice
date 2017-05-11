import math
inf = 1000000


def init(tree, node, start, end):
    tree[node] = inf
    if start != end:
        mid = (start + end) // 2
        init(tree, 2 * node, start, mid)
        init(tree, 2 * node + 1, mid + 1, end)


def minimum(tree, node, start, end, i, j):
    if end < i or j < start:
        return inf

    if i <= start and end <= j:
        return tree[node]

    mid = (start + end) // 2
    m1 = minimum(tree, 2 * node, start, mid, i, j)
    m2 = minimum(tree, 2 * node + 1, mid + 1, end, i, j)
    return min(m1, m2)


def update(tree, node, start, end, target_idx, value):
    if end < target_idx or target_idx < start:
        return

    tree[node] = min(tree[node], value)
    if start != end:
        mid = (start + end) // 2
        update(tree, 2 * node, start, mid, target_idx, value)
        update(tree, 2 * node + 1, mid + 1, end, target_idx, value)
    return


n = int(input())
line1 = input().split()
line2 = input().split()
line3 = input().split()

arr = [[0, 0, 0] * 1 for i in range(n + 1)]

score = 1
for id in line1:
    arr[int(id)][0] = score
    score += 1

score = 1
for id in line2:
    arr[int(id)][1] = score
    score += 1

score = 1
for id in line3:
    arr[int(id)][2] = score
    score += 1

arr.sort()

h = math.ceil(math.log2(n))
tree = [0] * (1 << (h + 1))  # tree[i] test C score of student who got i'th in test B

init(tree, 1, 1, n)
ans = 0
for i in range(1, n + 1):  # i for test A. thus at i'th count, we always compare student who got better score at test A.
    best = minimum(tree, 1, 1, n, 1, arr[i][1])  # best C score of student who
    if best > arr[i][2]:
        ans += 1

    update(tree, 1, 1, n, arr[i][1], arr[i][2])

print(ans)

