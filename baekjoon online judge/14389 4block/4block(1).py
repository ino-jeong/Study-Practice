# memory over....

nm = input().split()
n = int(nm[0])
m = int(nm[1])

min_return = -2**31

board_arr = []
for line in range(n):
    board_arr.append(input())

d = [[-1] * (3 << (m - 1)) for i in range(n * m)]  #d[num][state]


def block_check(num, state):
    if num == n * m and state == 0:
        return 0
    elif num >= n * m:
        return min_return

    if d[num][state] != -1:
        return d[num][state]

    i = int(num / m)  # vertical direction of board
    j = num % m  # horizontal direction of board

    ans = 0

    # 1. '1'is located in the board already
    if board_arr[i][j] != '.':
        ans = block_check(num + 1, (state >> 1)) + 1

    # 2. two block is occupied by '4'block at before line
    elif 0 < i and (state & 1) != 0 and (state & 2) != 0:
        ans = block_check(num + 2, (state >> 2))

    else:
        # 3. the location 'num' is empty. '1'block can be assigned
        if (state & 1) == 0:
            ans = block_check(num + 1, (state >> 1)) + 1

        # 4. if there is enough space, '4'block can be assigned
        if (num % m) < (m - 1) and int(num/m) < (n-1):
            if board_arr[i][j+1] == '.' and board_arr[i + 1][j] == '.' and board_arr[i + 1][j + 1] == '.':
                if state & 2 == 0 and state & (1<<m) == 0 and state & (1<<(m+1)) == 0:
                    ans = max(ans, block_check(num + 2, (state | 1 << m | 1 << (m + 1)) >> 2) + 16)

    d[num][state] = ans
    return ans


print(block_check(0, 0))
