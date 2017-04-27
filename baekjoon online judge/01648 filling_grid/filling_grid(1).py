'''

d[line][status] : number of grid filling with m X 'line', with 'status'
i.e. for full filled grid : status = 2**m - 1

fail.....

'''

nm = input().split()
n = int(nm[0])
m = int(nm[1])

d = [[-1] * (n + 1) for i in range(2**(m + 1))]  # d[line][status]


def get_next_status(initial_status, working_status, col, result_set):
    print('result set :', result_set)
    if col > m:
        result_set.append(working_status)
        return

    # can't pose block
    if initial_status & (1 << col) != 0:
        get_next_status(initial_status, working_status, col + 1, result_set)

    # 1. use block vertically
    get_next_status(initial_status, (working_status | (1 << col)), col + 1, result_set)

    # 2. use block horizontally
    if col + 1 <= m and (initial_status & (1 << (col + 1)) == 0):
        get_next_status(initial_status, working_status, col + 2, result_set)


def tiling(initial_status, line):
    print('&&&&&&&&&&&&', initial_status, line)
    if line == n:
        if initial_status == 0:
            return 1
        else:
            return 0

    if d[initial_status][line] != -1:
        return d[initial_status][line]

    ans = 0
    next_status_set = []
    get_next_status(initial_status, 0, 1, next_status_set)

    for next_line in next_status_set:
        print('****')
        ans += tiling(next_line, line + 1)

    d[initial_status][line] = ans
    return ans


print(tiling(0, 0))

print(d)
# print(d[0][n] % 9901)