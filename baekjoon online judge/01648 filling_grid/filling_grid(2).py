
nm = input().split()
n = int(nm[0])
m = int(nm[1])

d = [[-1] * (1 << m) for i in range(n * m)]  # d[line][status]


def tiling(num, status):
    if num == n * m and status == 0:
        return 1
    elif num >= n * m:
        return 0

    if d[num][status] != -1:
        return d[num][status]

    ans = 0

    if status & 2**0 != 0:
        ans = tiling(num + 1, (status >> 1))

    else:
        ans = tiling(num + 1, (status >> 1 | 1 << (m - 1)))
        if (num % m) < (m - 1) and (status & 2 == 0):
            ans += tiling(num + 2, (status >> 2))

    d[num][status] = ans % 9901
    return d[num][status]

print(tiling(0, 0))

