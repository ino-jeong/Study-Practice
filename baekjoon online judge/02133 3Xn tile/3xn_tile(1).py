n = int(input())

d = [[0] * 8 for i in range(n + 1)]
d[0][7] = 1

for cur in range(1, n + 1):
    d[cur][0] = d[cur - 1][7]
    d[cur][1] = d[cur - 1][6]
    d[cur][2] = d[cur - 1][5]
    d[cur][3] = d[cur - 1][7] + d[cur - 1][4]
    d[cur][4] = d[cur - 1][3]
    d[cur][5] = d[cur - 1][2]
    d[cur][6] = d[cur - 1][7] + d[cur - 1][1]
    d[cur][7] = d[cur - 1][0] + d[cur - 1][3] + d[cur - 1][6]

print(d[n][7])
