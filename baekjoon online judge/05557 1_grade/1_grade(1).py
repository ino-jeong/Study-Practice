n = int(input())
num_arr = [None]

line_input = input().split()
for num in line_input:
    num_arr.append(int(num))

memo_hash = {}

def count_formula(length, output):
    if length == 1:
        if num_arr[1] == output:
            return 1
        else:
            return 0

    if (length, output) in memo_hash:
        return memo_hash[(length, output)]

    ans = 0
    last_num = num_arr[length]

    if output - last_num >= 0:
        ans += count_formula(length - 1, output - last_num)

    if output + last_num <= 20:
        ans += count_formula(length - 1, output + last_num)

    memo_hash[(length, output)] = ans
    return ans

output = num_arr[n]
print(count_formula(n - 1, output))

