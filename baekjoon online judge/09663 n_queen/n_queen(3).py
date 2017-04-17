# def print_board(chk_arr):
#     for line in chk_arr:
#         print(line)
#     print('')

def queen_check(row, chk_arr, check_col, check_dig, check_dig2, n):

    # print_board(chk_arr)
    this_result = 0

    for i in range(n):
        # print('row :', row, 'col :', i)
        if check_queen(row, i, check_col, check_dig, check_dig2, n):
            if row == n - 1:
                return 1
            else:
                check_col[i] = 1
                check_dig[row + i] = 1
                check_dig2[row - i + n] = 1
                # print('row :', row, 'col :', i, 'queen check')
                this_result += queen_check(row + 1, chk_arr, check_col, check_dig, check_dig2, n)
                check_col[i] = 0
                check_dig[row + i] = 0
                check_dig2[row - i + n] = 0

    return this_result


def check_queen(row, col, check_col, check_dig, check_dig2, n):

    # vertical
    if check_col[col] == 1:
        return False


    if check_dig[row + col] == 1:
        return False

    if check_dig2[row - col + n] == 1:
        return False

    return True


n = int(input())

chk_arr = [[0] * n for i in range(n)]
check_col = [0] * n
check_dig = [0] * 2 * n
check_dig2 = [0] * 2 * n

result = queen_check(0, chk_arr, check_col, check_dig, check_dig2, n)

# print_board(chk_arr)

print(result)


