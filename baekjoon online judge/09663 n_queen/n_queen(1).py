# def print_board(chk_arr):
#     for line in chk_arr:
#         print(line)
#     print('')

def queen_check(row, chk_arr, n):

    # print_board(chk_arr)
    this_result = 0

    for i in range(n):
        # print('row :', row, 'col :', i)
        if check_queen(row, i, chk_arr, n):
            if row == n - 1:
                return 1
            else:
                chk_arr[row][i] = 1
                # print('row :', row, 'col :', i, 'queen check')
                this_result += queen_check(row + 1, chk_arr, n)
                chk_arr[row][i] = 0

    return this_result


def check_queen(row, col, chk_arr, n):

    # vertical
    for i in range(row):
        if chk_arr[i][col] == 1:
            return False

    i = row
    j = col
    while 0 <= i <= row and 0 <= j <= col:
        if i != row and j != col and chk_arr[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while 0 <= i <= row and col <= j < n:
        if i != row and j != col and chk_arr[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


n = int(input())

chk_arr = [[0] * n for i in range(n)]
result = queen_check(0, chk_arr, n)

# print_board(chk_arr)

print(result)


