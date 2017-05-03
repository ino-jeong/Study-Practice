def get_min_road():

    n = int(input())
    d = [[0] * n for i in range(n)]
    checker = [[1] * n for i in range(n)]

    for i in range(n):
        line = input().split()
        for j in range(n):
            d[i][j] = int(line[j])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or j == k:
                    continue

                if d[i][j] > d[i][k] + d[k][j]:
                    print(-1)
                    return

                if d[i][j] == d[i][k] + d[k][j]:
                    checker[i][j] = 0

    total_sum = 0
    for i in range(n):
        for j in range(n):
            if checker[i][j] == 1:
                total_sum += d[i][j]

    print(total_sum//2)

get_min_road()
