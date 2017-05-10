def range_sum(tree, i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)

    return i

def update(tree, i, diff):
    while i < len(tree):
        tree[i] += diff
        i += (i & -1)

nmk = input().split()
n = int(nmk[0])
m = int(nmk[1])
k = int(nmk[2])

nums = [0]
tree = [0] * (n + 1)

for i in range(1, n + 1):
    nums.append(int(input()))
    update(tree, i, nums[i])

m += k

for i in range(m):
    line_input = input().split()
    a, b, c = int(line_input[0]), int(line_input[1]), int(line_input[2])
    if a == 1:
        diff = c - nums[b]
        nums[b] = c
        update(tree, b, diff)
    else:
        print(range_sum(tree, c) - range_sum(tree, b - 1))

