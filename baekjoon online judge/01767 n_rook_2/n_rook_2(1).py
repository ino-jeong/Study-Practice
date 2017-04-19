'''
d[n][m][k] =
            d[n-1][m][k]
            + d[n-1][m-2][k-2] * m*(m-1)/2
            + d[n-1][m-1][k-1] * m
            + d[n-2][m-1][k-2] * m * (n-1)
'''


def calc_rook(n, m, k, d):

    if k == 0:
        return 1

    if n <= 0 or m <= 0 or n*m < k or k < 0:
        return 0

    if (n,m,k) in d:
        return d[(n,m,k)]

    d[(n, m, k)] = int(calc_rook(n-1, m, k, d) + calc_rook(n-1, m-2, k-2, d) * m * (m-1) / 2 + calc_rook(n-1, m-1, k-1, d) * m + calc_rook(n-2, m-1, k-2, d) * m * (n-1)) % 1000001

    return d[(n, m, k)]


def comb(m, k):
    com = [0] * (m+1)
    com[0] = 1
    com[1] = 1
    last_idx = 1

    if m == 1:
        return com[k]
    for i in range(m-1):

        for j in range(last_idx,-1,-1):
            com[j+1] += com[j]
        last_idx += 1

    return com[k]


n = int(input())
m = int(input())
k = int(input())
d={}

print(calc_rook(n, m, k, d))

