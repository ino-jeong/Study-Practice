n = int(input())

d = [[0] * n for i in range(n)]
for i in range(n):
    line = input().split()
    for j in range(n):
        if int(line[j]) == 1:
            d[i][j] = int(line[j])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k] != 0 and d[k][j] != 0:
                d[i][j] = 1


for line in d:
    for num in line:
        print(num, end=' ')
    print('')
