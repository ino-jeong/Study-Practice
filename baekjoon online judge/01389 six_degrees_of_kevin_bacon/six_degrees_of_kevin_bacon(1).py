inf = 100000

nm = input().split()
n = int(nm[0])
m = int(nm[1])

d = [[inf] * n for i in range(n)]
for i in range(n):
    d[i][i] = 0

degrees = [0] * n

for line in range(m):
    line_input = input().split()
    i = int(line_input[0]) - 1
    j = int(line_input[1]) - 1

    d[i][j] = 1
    d[j][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

for i in range(n):
    for j in range(n):
        if d[i][j] > 0 and d[i][j] != inf:
            degrees[i] += d[i][j]


print(degrees.index(min(degrees)) + 1)

