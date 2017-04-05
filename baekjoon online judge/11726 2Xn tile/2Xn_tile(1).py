'''
d(n) = number of methods covering 2 x n size by small tiles
d(n) =
        d(n-1) +  # just adding 1 more tile
        d(n-2)    # adding 2 tile horizontally
'''

def d(n, memo):
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n+1):
        memo[i] = (memo[i-1] + memo[i-2]) % 10007
    return memo[n]

n = int(input())
memo = {}
print(d(n, memo))