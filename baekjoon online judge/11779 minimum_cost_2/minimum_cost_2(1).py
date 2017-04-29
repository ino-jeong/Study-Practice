# run time error....


inf = 1000000000

n = int(input())
m = int(input())


buses = [[0] * 3 for i in range(m)]
for i in range(m):
    line_input = input().split()
    buses[i][0] = int(line_input[0])
    buses[i][1] = int(line_input[1])
    buses[i][2] = int(line_input[2])

se = input().split()
s = int(se[0])
e = int(se[1])

dist = [inf] * (n + 1)
dist[s] = 0

route = [-1] * (n + 1)
check = [0] * (n + 1)  # 0 : not checked  /  1 : checked (visited)


def get_min_dist():
    cur_cost = inf + 1
    min_index = 1
    for i in range(1, n+1):
        if check[i] == 0 and dist[i] < cur_cost:
            min_index = i
            cur_cost = dist[i]

    return min_index


for i in range(n):
    u = get_min_dist()
    check[u] = 1

    for j in range(m):
        if buses[j][0] == u:
            v = buses[j][1]
            c = buses[j][2]

            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                route[v] = u

print(dist[e])

route_stack = []

prev = e
count = 0
while prev != s:
    route_stack.append(prev)
    count += 1
    prev = route[prev]

route_stack.append(s)
count += 1

print(count)

route_str = str(route_stack.pop())
for i in range(len(route_stack)):
    route_str = route_str + ' ' + str(route_stack.pop())

print(route_str)

