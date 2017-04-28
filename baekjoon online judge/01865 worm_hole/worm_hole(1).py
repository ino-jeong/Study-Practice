inf = 100000


def wormhole_check(n, m, w, roads, worms, dist):

    # negative_cycle = False

    for i in range(n):

        # 1. roads, original direction
        for j in range(m):
            u = roads[j][0]
            v = roads[j][1]
            c = roads[j][2]

            if dist[u] != inf and dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                if i == n-1:
                    print('YES')
                    return

        # 2. roads, opposite direction
        for j in range(m):
            u = roads[j][1]
            v = roads[j][0]
            c = roads[j][2]

            if dist[u] != inf and dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                if i == n - 1:
                    print('YES')
                    return

                # 3. worm holes
        for j in range(w):
            u = worms[j][0]
            v = worms[j][1]
            c = worms[j][2]

            if dist[u] != inf and dist[v] > dist[u] - c:
                dist[v] = dist[u] - c
                if i == n-1:
                    print('YES')
                    return

    print('NO')
    return


t = int(input())
for case in range(t):
    nmw = input().split()
    n = int(nmw[0])
    m = int(nmw[1])
    w = int(nmw[2])

    dist = [inf] * n
    dist[0] = 0

    roads = [[0] * 3 for i in range(m)]
    for road in range(m):
        line = input().split()
        roads[road][0] = int(line[0]) - 1
        roads[road][1] = int(line[1]) - 1
        roads[road][2] = int(line[2])

    worms = [[0] * 3 for i in range(w)]
    for worm in range(w):
        line = input().split()
        worms[worm][0] = int(line[0]) - 1
        worms[worm][1] = int(line[1]) - 1
        worms[worm][2] = int(line[2])

    wormhole_check(n, m, w, roads, worms, dist)

