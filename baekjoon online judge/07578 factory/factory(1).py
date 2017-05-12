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
        idx += (idx & - idx)


n = int(input())

a = [0]
line_input = input().split()
for numb in line_input:
    a.append(int(numb))

b = {}
line_input = input().split()
i = 1
for numb in line_input:
    b[int(numb)] = i
    i += 1

ans = 0
tree = [0] * (n + 1)
for i in range(1, n + 1):
    # 1. a에서 순서대로 기기를 check
    now = a[i]

    # 2. b상에서 해당 기기보다 뒤에 있으면서 이미 tree에 check된 기기 수의 합 구함
    now_num = b[now]
    ans += range_sum(tree, now_num + 1, n)

    # 3. 방금 꺼낸 a도 tree에 check 해둠
    update(tree, now_num, 1, n)

print(ans)

