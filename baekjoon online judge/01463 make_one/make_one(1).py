def make_one(n, memo):
    '''
    make_one(n) = number of minimum operation from n to 1
    make_one(n) =
                    min of :
                        make_one(n-1) + 1,
                        make_one(n/2) + 1,
                        make_one(n/3) + 1
    '''
    memo[1] = 0
    for i in range(2, n+1):
        memo[i] = memo[i-1] + 1

        if i % 2 == 0 and i/2 in memo:
            if memo[i] > memo[i / 2] + 1:
                memo[i] = memo[i / 2] + 1

        if i % 3 == 0 and i/3 in memo:
            if memo[i] > memo[i / 3] + 1:
                memo[i] = memo[i / 3] + 1

    return memo[n]

n = int(input())
memo = {}
result = make_one(n, memo)

print(result)