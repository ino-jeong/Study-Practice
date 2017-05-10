nm = input().split()
n = int(nm[0])
m = int(nm[1])

nums = input().split()
s = [0] * (n + 1)
s[1] = int(nums[0])

for i in range(2, n + 1):
    s[i] = int(nums[i - 1]) + s[i-1]

order_query = []
for i in range(m):
    line_input = input().split()
    i, j = int(line_input[0]), int(line_input[1])
    order_query.append((i, j))

for (i,j) in order_query:
    print(s[j] - s[i - 1])

