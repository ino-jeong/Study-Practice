n, k = map(int, input().split())
d = {}

def find_array(length, last):
    if (length, last) in d:
        return d[(length, last)]

    if not 1 <= last <= k:
        return 0

    if length >= n:
        return 1

    ans = 0
    for num in range(1, k + 1):
        if last % num != 0: # last > num and
            ans += find_array(length + 1, num)
        elif last <= num:
            ans += find_array(length + 1, num)

    d[(length, last)] = ans % 1000000007
    return d[(length, last)]


print(find_array(0, 1))
