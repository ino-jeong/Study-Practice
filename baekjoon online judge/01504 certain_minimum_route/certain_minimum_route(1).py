import sys

inf = 1000000

# ne = input().split()
ne = sys.stdin.readline().split()
n = int(ne[0])
e = int(ne[1])

start = 0
end = (n-1)

edges = [[inf] * n for i in range(n)]
for edge in range(e):
    # line_input = input().split()
    line_input = sys.stdin.readline().split()
    # edges.append([int(line_input[0]) - 1, int(line_input[1]) - 1, int(line_input[2])])
    # edges.append([int(line_input[1]) - 1, int(line_input[0]) - 1, int(line_input[2])])
    s = int(line_input[0]) - 1
    e = int(line_input[1]) - 1
    c = int(line_input[2])

    if edges[s][e] > c:
        edges[s][e] = c
        edges[e][s] = c


# ab = input().split()
ab = sys.stdin.readline().split()
a = int(ab[0]) - 1
b = int(ab[1]) - 1


def get_min_cost_vertex(dist, check):
    min_vertex = 0
    min_cost = inf + 1

    for i in range(n):
        if check[i] == 0 and dist[i] < min_cost:
            min_cost = dist[i]
            min_vertex = i

    return min_vertex


def min_route(start, end):

    dist = [inf] * n
    dist[start] = 0
    check = [0] * n

    for i in range(n):
        u = get_min_cost_vertex(dist, check)
        check[u] = 1
        for v in range(n):
            c = edges[u][v]
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c

    return dist


start_cost = min_route(start, end)
a_cost = min_route(a, end)
b_cost = min_route(b, end)

route_1 = start_cost[a] + a_cost[b] + b_cost[end]
route_2 = start_cost[b] + b_cost[a] + a_cost[end]

if (route_1 >= inf and route_2 >= inf):
    print(-1)
elif route_1 < route_2:
    print(route_1)
else:
    print(route_2)
