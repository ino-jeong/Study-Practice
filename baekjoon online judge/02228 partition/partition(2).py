def partition(n, m, seq, sum_hash, d):
    if (n, m) in d:
        return d[(n, m)]

    if m == 0: # if partition is zero(0), sum of partition is also zero(0)
        return 0

    if n <= 0: # number index should not under 0... thus in this case return value should be penalty
        return -32768 * 100

    # n'th number is not included in m'th group
    result_cost = partition(n - 1, m, seq, sum_hash, d)

    # n'th number is included in m'th group
    for k in range(0, n - 2 * m + 2):
        temp_result = partition(n - k - 2, m - 1, seq, sum_hash, d) + sum_hash[n] - sum_hash[n - k - 1]
        result_cost = max(result_cost, temp_result)

    d[(n, m)] = result_cost
    return d[(n, m)]


def seq_sum(seq, sum_hash, n):
    sum_hash[-1] = 0
    sum_hash[0] = 0
    for i in range(1, n + 1):
        sum_hash[i] = sum_hash[i - 1] + seq[i]


nm = input().split()
n = int(nm[0])
m = int(nm[1])

seq = [None]  # to avoid starting it's index from 0, prevent confusing.
sum_hash = {}
d = {}

for i in range(n):
    num = int(input())
    seq.append(num)

seq_sum(seq, sum_hash, n)

print(partition(n, m, seq, sum_hash, d))


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