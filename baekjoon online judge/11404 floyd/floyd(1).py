inf = 1000000

n = int(input())
m = int(input())

d = [[inf] * n for i in range(n)]
for i in range(n):
    d[i][i] = 0

for i in range(m):
    line = input().split(' ')
    d[int(line[0]) - 1][int(line[1]) - 1] = min(d[int(line[0]) - 1][int(line[1]) - 1], int(line[2]))


for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print('')

