
nm = input().split()
n = int(nm[0])
m = int(nm[1])

tofu_arr = []
for i in range(n):
    line_input = input()
    tofu_arr.append(line_input)

d = [[-1] * (1 << m) for i in range(n*m)]

tofu_price = {
    'AA': 10, 'AB': 8, 'AC': 7, 'AD': 5, 'AF': 1,
    'BA': 8, 'BB': 6, 'BC': 4, 'BD': 3, 'BF': 1,
    'CA': 7, 'CB': 4, 'CC': 3, 'CD': 2, 'CF': 1,
    'DA': 5, 'DB': 3, 'DC': 2, 'DD': 2, 'DF': 1,
    'FA': 1, 'FB': 1, 'FC': 1, 'FD': 1, 'FF': 0
}


def tofu_cut(num, state):
    if num == n * m and state == 0:
        return 0
    elif num >= n * m:
        return -2*31

    if d[num][state] != -1:
        return d[num][state]

    ans = -2**31
    if state & 1 != 0:
        ans = tofu_cut(num + 1, (state >> 1))
    else:
        # 1. throw away 'num' ans 1 X 1 tofu cut
        ans = tofu_cut(num + 1, (state >> 1))

        # 2. cut 2 X 1
        if num + m < n * m:
            price_of_this_cut = get_price(num, num + m)
            ans = max(ans, tofu_cut(num + 1, (state >> 1 | 1 << (m - 1))) + price_of_this_cut)

        # 3. cut 1 X 2
        if (num % m) < (m - 1) and state & 2 == 0:
            price_of_this_cut = get_price(num, num + 1)
            ans = max(ans, tofu_cut(num + 2, (state >> 2)) + price_of_this_cut)

    d[num][state] = ans
    return ans


def get_price(num1, num2):
    # get tag of each cut (num1 and num2) which data type is string
    tag1 = tofu_arr[int(num1 / m)][num1 % m]
    tag2 = tofu_arr[int(num2 / m)][num2 % m]
    tag = tag1 + tag2 # string concatenation

    return tofu_price[tag]

print(tofu_cut(0, 0))

