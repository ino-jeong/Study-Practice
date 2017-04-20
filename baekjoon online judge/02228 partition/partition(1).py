def partition(n, m, seq, d):
    if (n, m) in d:
        return d[(n, m)]

    if m == 0:
        return 0

    if n <= 0:
        return -32768 * 100

    # n'th number is not included in m'th group
    result_cost = partition(n-1, m, seq, d)

    # n'th number is included in m'th group

    num_sum = 0
    for k in range(n, 0, -1):
        num_sum += seq[k]
        temp_result = partition(k - 2, m - 1, seq, d) + num_sum
        result_cost = max(result_cost, temp_result)

    d[(n,m)] = result_cost
    return d[(n, m)]


nm = input().split()
n = int(nm[0])
m = int(nm[1])

seq = [None] #to avoid starting it's index from 0, prevent confusing.
d = {}

for i in range(n):
    num = int(input())
    seq.append(num)

print(partition(n, m, seq, d))


'''
10 2
-1
-2
-3
-4
-5
-6
-7
-8
-9
-10
'''