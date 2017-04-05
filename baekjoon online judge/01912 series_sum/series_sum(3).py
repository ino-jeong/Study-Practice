n = int(input())
sequence = input().split(' ')

d = [None] * 100000

for i in range(n):
    d[i] = int(sequence[i])
    if i == 0:
        continue
    elif d[i] < d[i - 1] + int(sequence[i]):
        d[i] = d[i - 1] + int(sequence[i])

max_result = d[0]
for j in range(n):
    max_result = max(max_result, d[j])

print(max_result)