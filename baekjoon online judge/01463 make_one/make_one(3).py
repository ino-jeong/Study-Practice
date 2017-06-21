# 100만 ? = 1,000,000
'''
d[n] = n을 1로 만드는데 드는 최소 연산수.

'''

d = [0] * (10**6)

def make_one(n):
    if n == 1:
        return 0

    if d[n] > 0:
        return d[n]

    d[n] = make_one(n-1) + 1

    if n%2 == 0:
        d[n] = min(d[n], make_one(n//2) + 1)

    if n%3 == 0:
        d[n] = min(d[n], make_one(n//3) + 1)

    return d[n]

n = int(input())
print(make_one(n))

