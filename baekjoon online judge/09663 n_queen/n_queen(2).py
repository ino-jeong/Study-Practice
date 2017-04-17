# time over

def check(row, col, chk_arr, n):
    for i in range(n):
        if i == row:
            continue
        if chk_arr[i][col]:
            return False

    x = row - 1
    y = col - 1
    while x >= 0 and y >= 0:
        if chk_arr[x][y] == True:
            return False
        x -= 1
        y -= 1

    x = row - 1
    y = col + 1
    while x >= 0 and y < n:
        if chk_arr[x][y] == True:
            return False
        x -= 1
        y += 1

    return True

def calc(row, chk_arr, ans, n):
    if row == n:
        ans[0] += 1

    for col in range(n):
        chk_arr[row][col] = True
        if check(row, col, chk_arr, n):
            calc(row + 1, chk_arr, ans, n)
        chk_arr[row][col] = False


ans = [0]
n = int(input())
chk_arr = [[False] * n for i in range(n)]
calc(0, chk_arr, ans, n)
print(ans[0])
