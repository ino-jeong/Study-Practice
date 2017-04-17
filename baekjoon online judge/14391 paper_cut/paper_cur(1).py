def check_cut(paper, checker, i, j, n, m, max_sum):
    if i == n-1 and j == m-1:
        checker[i][j] = 1
        max_sum[0] = max(max_sum[0], cal_sum(paper, checker, n, m))

        checker[i][j] = 0
        max_sum[0] = max(max_sum[0], cal_sum(paper, checker, n, m))
        return

    if j == m-1: #to the next row
        next_j = 0
        next_i = i + 1
    else:
        next_j = j + 1
        next_i = i

    # 0 : horizontal / 1 : vertical
    # 1. make (i,j) vertical cut
    checker[i][j] = 1
    check_cut(paper, checker, next_i, next_j, n, m, max_sum)
    checker[i][j] = 0

    # 2. make (i,j) horizontal cut (original state)
    check_cut(paper, checker, next_i, next_j, n, m, max_sum)


def cal_sum(paper, checker, n, m):
    #1. check horizontal numbers
    num_sum = 0
    for i in range(n):
        num = ''
        for j in range(m):
            if checker[i][j] == 0:
                num = num + paper[i][j]
            elif checker[i][j] == 1 and num != '':
                num_sum += int(num)
                num = ''
        if num != '':
            num_sum += int(num)

    #2. check vertical numbers
    for j in range(m):
        num = ''
        for i in range(n):
            if checker[i][j] == 1:
                num = num + paper[i][j]
            elif checker[i][j] == 0 and num != '':
                num_sum += int(num)
                num = ''
        if num != '':
            num_sum += int(num)

    return num_sum


nm = input().split()
n = int(nm[0])
m = int(nm[1])

paper = [['0'] * m for i in range(n)]
checker = [[0] * m for i in range(n)]

for i in range(n):
    line_input = input()
    for j in range(m):
        paper[i][j] = line_input[j]

max_sum = [0]
check_cut(paper, checker, 0, 0, n, m, max_sum)

print(max_sum[0])

