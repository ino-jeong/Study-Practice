'''
d(n) = no. of methods representing n by only sum of 1 or 2 or 3

then

d(n) =
        d(n-1) + 1 +  (by adding 1)
        d(n-2) + 1 +  (by adding 2)
        d(n-3) + 1    (by adding 3)
'''

def d(n, memo):
    if n <= 0:
        return 0
    if n in memo:
        return memo[n]
    result = 0

    if d(n-1, memo) > 0:
        result += d(n-1, memo)
    if d(n-2, memo) > 0:
        result += d(n-2, memo)
    if d(n-3, memo) > 0:
        result += d(n-3, memo)

    return result

memo = {}
memo[1] = 1
memo[2] = 2
memo[3] = 4
'''
if n == 1:  # 1
    return 1
if n == 2:  # 1,1 / 2
    return 2
if n == 3:  # 1,1,1 / 1,2 / 2,1 / 3
    return 4
'''

cases = int(input())
for c in range(cases):
    line_input = int(input())
    print(d(line_input, memo))