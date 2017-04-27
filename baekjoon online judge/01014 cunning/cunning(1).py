# fail

def max_student(row, cur_status):

    print('***',row, cur_status)

    if memo_arr[row][cur_status] != -1:
        return memo_arr[row][cur_status]

    if row == n - 1:
        return count_status(cur_status)

    # for new_student....
    new_status = 0
    for i in range(1, m + 1):
        if check(row + 1, i, m, cur_status, new_status):
            new_status = new_status | (1 << i)

    cur_student = count_status(cur_status)
    result = cur_student + max_student(row + 1, new_status)

    memo_arr[row][cur_status] = result
    return result


def check(row, i, m, previous_line, new_line):
    if class_map[row][i] != '.':
        return False

    if 1 < i and (previous_line & (1 << (i-1))) != 0:
        return False

    if m > i and (previous_line & (1 << (i+1))) != 0:
        return False

    if 3 <= i and new_line & (1 << (i-1)) != 0:
        return False

    return True


def count_status(status):
    total = 0
    count_student = bin(status).lstrip('0b')

    for i in range(len(count_student)):
        total += int(count_student[i])

    return total


def get_initial_status(i):
    result = 0
    for j in range (i, m + 1):
        if class_map[0][j] != '.':
            return -1
        if 3 <= j and result & (1 << (j-1)) != 0:
            return -1
        result = result | 2**(j-1)

    if result == 0:
        return -1
    print('%%%', i, result)
    return result


c = int(input())
for case in range(c):
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    class_map = []
    memo_arr = [[-1] * (2**(m+1))] * n

    for line in range(n):
        line_input = 'x'
        line_input += input()
        class_map.append(line_input)

    print(class_map)

    result = 0

    for i in range(1, m + 1):
        status = get_initial_status(i)
        if status != -1:
            temp = max_student(0, status)
            print('temp :',temp)
            result = max(result, temp)

    print(result)



