def init(nums, tree, n):
    # 0. 모든 배열의 index는 1부터 시작
    tree[1] = nums[1]

    for i in range(2, n + 1):
        # 1. 자기 자신(i)을 tree[i]에 저장
        tree[i] = nums[i]
        last_bit = i & -i

        # 2. 자기 자신을 저장했으므로 i의 last_bit에서 -1
        last_bit -= 1
        k = i - 1

        # 3. tree[i-1]를 중복 합하고, i-1의 last bit만큼 last_bit 에서 뺀다.
        # 4. 3번을 해당숫자가 0이 될 때까지 반복한다.
        while last_bit > 0:
            tree[i] += tree[k]
            last_bit -= (k & -k)
            k -= (k & -k)


def update(tree, n, i, num):
    delta = num - tree[i]
    while i <= n:
        tree[i] += delta
        i += (i & -i)


def sum_query(tree, i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)

    return ans


nmk = input().split()
n = int(nmk[0])
m = int(nmk[1])
k = int(nmk[2])

nums = [0]
for i in range(n):
    nums.append(int(input()))

tree = [0] * (n + 1)

order_queries = []

for i in range(m+k):
    line_input = input().split()
    a, b, c = int(line_input[0]), int(line_input[1]), int(line_input[2])
    order_queries.append((a, b, c))

init(nums, tree, n)

for (a, b, c) in order_queries:
    if a == 1:
        update(tree, n, b, c)
    else:
        print(sum_query(tree, c) - sum_query(tree, b - 1))

