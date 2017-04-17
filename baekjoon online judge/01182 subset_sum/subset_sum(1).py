def sum_check(num_set, cur_sum, idx, n, s, count, empty_set):
    if idx >= n:
        if cur_sum == s and empty_set != 0:
            count[0] += 1
        return

    # include i'th number in the sum
    sum_check(num_set, cur_sum + num_set[idx], idx + 1, n, s, count, empty_set + 1)

    # exclude i'th number
    sum_check(num_set, cur_sum, idx + 1, n, s, count, empty_set + 0)

    pass


line = input().split()
n = int(line[0])
s = int(line[1])

line = input().split()
num_set = []
for num in line:
    num_set.append(int(num))

count = [0]

sum_check(num_set, 0, 0, n, s, count, 0)
print(count[0])
