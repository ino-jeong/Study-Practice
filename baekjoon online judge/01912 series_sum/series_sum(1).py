'''
d(n) = max sum in the sequence which is end at n'th number
d(n) = max(
            d(n-1) + n,
            n
            )
'''

def d(n, sequence, memo):
    if n == 1:
        return int(sequence[0])
    if n in memo:
        return memo[n]

    result = max(
        d(n-1, sequence, memo) + int(sequence[n-1]),
        int(sequence[n-1])
    )
    memo[n] = result
    return memo[n]


n = int(input())
sequence = input().split(' ')
memo = {}
memo[1] = int(sequence[0])

d(n, sequence, memo)

max_result = memo[1]
for i in range(1, n+1):
    if max_result < memo[i]:
        max_result = memo[i]

print(max_result)
