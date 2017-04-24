'''

d[length][num][S] : stair number of 'length', end at 'num' with used number set 'S'
d[length][num][S] = d[length - 1][num + 1][S - (num + 1)] + d[length - 1][num - 1][S - (num - 1)]
iff num + 1 and num - 1 borh in range of 0 <= number <= 9

'''

n = int(input())
mod = 1000000000

memo_arr = [[[-1] * 1024 for j in range(10)] for i in range(101)]

def get_stair_num(length, end_num, rest_num_set):
    if length == 1:
        if end_num != 0 and rest_num_set == 0:
            return 1
        else:
            return 0

    if memo_arr[length][end_num][rest_num_set] != -1:
        return memo_arr[length][end_num][rest_num_set]

    result = 0

    if end_num + 1 <= 9:
        before_num = end_num + 1
        result += get_stair_num(length - 1, end_num + 1, rest_num_set & ~ (1<<before_num)) % mod

    if end_num - 1 >= 0:
        before_num = end_num - 1
        result += get_stair_num(length - 1, end_num - 1, rest_num_set & ~ (1<<before_num)) % mod

    memo_arr[length][end_num][rest_num_set] = result % mod
    return memo_arr[length][end_num][rest_num_set]


total_result = 0
start_num_set = int('0b1111111111', 2)
for i in range(10):
    total_result += get_stair_num(n, i, start_num_set & ~(1<<i)) % mod

print(total_result % mod)


