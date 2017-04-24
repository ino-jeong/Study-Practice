'''

d[length][num] : stair number with 'length', end at 'num'
d[length][num] = d[length - 1][num + 1] + d[length - 1][num - 1]
iff num + 1 and num - 1 borh in range of 0 <= number <= 9

'''

n = int(input())
mod = 1000000000

memo_arr = [[-1] * 10 for i in range(101)]

def get_stair_num(length, end_num):
    if length == 1:
        if end_num != 0:
            return 1
        else:
            return 0

    if memo_arr[length][end_num] != -1:
        return memo_arr[length][end_num]

    result = 0

    if end_num + 1 <= 9:
        result += get_stair_num(length - 1, end_num + 1) % mod

    if end_num - 1 >= 0:
        result += get_stair_num(length - 1, end_num - 1) % mod

    memo_arr[length][end_num] = result % mod
    return memo_arr[length][end_num]


total_result = 0
for i in range(10):
    total_result += get_stair_num(n, i) % mod

print(total_result % mod)


