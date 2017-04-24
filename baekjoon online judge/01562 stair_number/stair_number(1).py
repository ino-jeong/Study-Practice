'''

d[length][num] : stair number with 'length', end at 'num'
d[length][num] = d[length - 1][num + 1] + d[length - 1][num - 1]
iff num + 1 and num - 1 borh in range of 0 <= number <= 9

'''

n = int(input())

memo_arr = [[0] * 10 for i in range(101)]

def get_stair_num(length, end_num):
    if length == 1:
        if end_num != 0:
            return 1
        else:
            return 0

    if memo_arr[length][end_num] != 0:
        return memo_arr[length][end_num]

    result = 0

    if end_num + 1 <= 9:
        result += get_stair_num(length - 1, end_num + 1)

    if end_num - 1 >= 0:
        result += get_stair_num(length - 1, end_num - 1)

    memo_arr[length][end_num] = result % 1000000000
    return memo_arr[length][end_num]


total_result = 0
for i in range(10):
    total_result += get_stair_num(n, i)

print(total_result)


