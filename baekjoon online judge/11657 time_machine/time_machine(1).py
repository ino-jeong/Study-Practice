nm = input().split()
n = int(nm[0])
m = int(nm[1])

inf = 100000
negative_cycle = False

dist = [inf] * n
dist[0] = 0

edges = [[0] * 3 for i in range(m)]
for i in range(m):
    line_input = input().split()
    edges[i][0], edges[i][1], edges[i][2] = int(line_input[0]) - 1, int(line_input[1]) - 1, int(line_input[2])

for i in range(n):
    for j in range(m):
        u = edges[j][0]
        v = edges[j][1]
        c = edges[j][2]

        if dist[u] != inf and (dist[v] > dist[u] + c):
            dist[v] = dist[u] + c

            if i == n-1 : # n'th loop (starting from 0...)
                negative_cycle = True

if negative_cycle:
    print(-1)
else:
    for i in range(1, n):
        cost = dist[i]
        if cost == inf:
            print(-1)
        else:
            print(cost)


