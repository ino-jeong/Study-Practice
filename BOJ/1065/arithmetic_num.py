def is_arithmetic_num(num):
    result = True
    num_arr = []

    while num != 0:
        num_arr.append(num % 10)
        num //= 10

    if len(num_arr) <= 2:
        result = True
        return result
    else:
        gap = num_arr[0] - num_arr[1]
        for i in range(1, len(num_arr)-1):
            if (num_arr[i] - num_arr[i+1]) != gap:
                result = False
                break

    return result

n = int(input())

count = 0
for x in range(1, n + 1):
    if is_arithmetic_num(x) is True:
        count += 1

print(count)
