n, k = map(int, input().split())
d = {}

def find_array(length, last):
    if (length, last) in d:
        return d[(length, last)]

    if not 1 <= last <= k:
        return 0

    if length == 1:
        return 1

    ans = 0
    for num in range(last + 1, k + 1):
        if num % last == 0:
            ans += find_array(length - 1, num)

    d[(length, last)] = ans
    return d[(length, last)]


total_case = n * (k**2)
sub_case = 0
for i in range(1, k + 1):
    sub_case += find_array(n, i)

print(total_case - sub_case)
