inf = 1000000

n = int(input())
m = int(input())

d = [[inf] * n for i in range(n)]
for i in range(n):
    d[i][i] = 0

route = [[[0, '']] * n for i in range(n)]

for i in range(m):
    line = input().split()
    if d[int(line[0]) - 1][int(line[1]) - 1] > int(line[2]):
        d[int(line[0]) - 1][int(line[1]) - 1] = int(line[2])
        route[int(line[0]) - 1][int(line[1]) - 1] = [2, line[0] + ' ' + line[1]]


for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                route[i][j][0] = route[i][k][0] + route[k][j][0] - 1
                route[i][j][1] += str(k)


for i in range(n):
    for j in range(n):
        print(d[i][j], end=' ')
    print('')

for i in range(n):
    for j in range(n):
        print(route[i][j][0], route[i][j][1])
