def get_sum(tree, idx):
    ans = 0

    while idx > 0:
        ans += tree[idx]
        idx -= (idx & -idx)

    return ans


def range_sum(tree, i, j):
    if i > j:
        return 0

    return get_sum(tree, j) - get_sum(tree, i - 1)


def update(tree, idx, value, n):
    while idx <= n:
        tree[idx] += value
        idx += (idx & -idx)


n = int(input())
line_input = input().split()
a = [[0, 0]]
tree = [0] * (n + 1)
for i in range(n):
    work_time = int(line_input[i])
    a.append([work_time, i + 1])
    update(tree, i + 1, 1, n)

a.sort()

ans = [0] * (n + 1)
total_time = 0
last_work_time = 0
remain_work = n  # number of word to be done

for i in range(n):
    [work_time, work_num] = a[i + 1]

    total_time += (work_time - last_work_time) * remain_work
    work_done_now = total_time - range_sum(tree, work_num + 1, n)
    remain_work -= 1
    last_work_time = work_time

    ans[work_num] = work_done_now
    update(tree, work_num, -1, n)

for done_time in ans[1:]:
    print(done_time)