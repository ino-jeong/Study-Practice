def d(n, sequence, memo):
    if n == 1:
        return memo[0]

    for i in range(1, n):
        memo[i] = max(memo[i - 1] + int(sequence[i]), int(sequence[i]))

    max_result = memo[0]
    for i in range(n):
        max_result = max(max_result, memo[i])

    return max_result


n = int(input())
sequence = input().split(' ')
memo = [None] * 100000
memo[0] = int(sequence[0])

print(d(n, sequence, memo))
