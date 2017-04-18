def check_maze(map_arr, R_i, R_j, B_i, B_j, count, min_count, visit_hash):
    if count >= 10:
        return

    visit_hash[(R_i, R_j, B_i, B_j)] = True
    directions = ['right', 'left', 'up', 'down']

    # print('')
    # for l in range(n):
    #     print(map_arr[l])

    for dir in directions:
        checker, nR_i, nR_j, nB_i, nB_j = move_ball(map_arr, R_i, R_j, B_i, B_j, dir)
        # print('\n in the for loop :')
        # for l in range(n):
        #     print(map_arr[l])
        print(checker)

        if (nR_i, nR_j, nB_i, nB_j) == (R_i, R_j, B_i, B_j) or ((nR_i, nR_j, nB_i, nB_j) in visit_hash and checker != 1):
            continue

        print('****', R_i, R_j, B_i, B_j, 'to', dir, nR_i, nR_j, nB_i, nB_j, (nR_i == R_i and nR_j == R_j and nB_i == B_i and nB_j == B_j))

        if checker == 1:
            min_count[0] = min(count+1, min_count[0])
            print('^^^ min count :', min_count[0])

        elif checker == 0:
            check_maze(map_arr, nR_i, nR_j, nB_i, nB_j, count+1, min_count, visit_hash)

            # map_arr[R_i][R_j], map_arr[nR_i][nR_j] = map_arr[nR_i][nR_j], map_arr[R_i][R_j]
            # map_arr[B_i][B_j], map_arr[nB_i][nB_j] = map_arr[nB_i][nB_j], map_arr[B_i][B_j]

            if dir == 'left':
                dump, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'right')
            elif dir == 'right':
                dump, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'left')
            elif dir == 'up':
                dump, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'down')
            else:
                dump, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'up')

    return


def check_ball_position(map_arr):
    n = len(map_arr)
    m = len(map_arr[0])

    R_i, R_j = (0, 0)
    B_i, B_j = (0, 0)

    for i in range(n):
        for j in range(m):
            if map_arr[i][j] == 'R':
                R_i, R_j = (i, j)
            elif map_arr[i][j] == 'B':
                B_i, B_j = (i, j)

    return R_i, R_j, B_i, B_j


def move_ball(map_arr, R_i, R_j, B_i, B_j, direction):

    n = len(map_arr)
    m = len(map_arr[0])

    #1. direction = left
    if direction == 'left':
        while (R_j - 1 > 0 and (map_arr[R_i][R_j - 1] == '.' or map_arr[R_i][R_j - 1] == 'O')) or (B_j - 1 > 0 and (map_arr[B_i][B_j - 1] == '.' or map_arr[B_i][B_j - 1] == 'O')):
            # print('^**^ map_arr[R_i][R_j - 1] :',map_arr[R_i][R_j - 1], 'map_arr[R_i][R_j] :', map_arr[R_i][R_j])
            # print('^**^ map_arr[B_i][B_j - 1] :',map_arr[B_i][B_j - 1], 'map_arr[B_i][B_j] :', map_arr[B_i][B_j])
            # tR_i, tR_j, tB_i, tB_j = check_ball_position(map_arr)
            # print('^*tt*^ tR_i, tR_j :', tR_i, tR_j)
            # print('^*tt*^ tB_i, tB_j :', tB_i, tB_j)
            if map_arr[R_i][R_j - 1] == '.':
                map_arr[R_i][R_j - 1], map_arr[R_i][R_j] = map_arr[R_i][R_j], map_arr[R_i][R_j - 1]
                R_j -= 1
            elif map_arr[R_i][R_j - 1] == 'O':
                return 1, R_i, R_j, B_i, B_j

            if map_arr[B_i][B_j - 1] == '.':
                map_arr[B_i][B_j - 1], map_arr[B_i][B_j] = map_arr[B_i][B_j], map_arr[B_i][B_j - 1]
                B_j -= 1
            elif map_arr[B_i][B_j - 1] == 'O':
                return -1, R_i, R_j, B_i, B_j

        return 0, R_i, R_j, B_i, B_j


    #2. direction = right
    if direction == 'right':
        while (R_j + 1 < m - 1 and (map_arr[R_i][R_j + 1] == '.' or map_arr[R_i][R_j + 1] == 'O')) or (B_j + 1 < m - 1 and (map_arr[B_i][B_j + 1] == '.' or map_arr[B_i][B_j + 1] == 'O')):
            if map_arr[R_i][R_j + 1] == '.':
                map_arr[R_i][R_j + 1], map_arr[R_i][R_j] = map_arr[R_i][R_j], map_arr[R_i][R_j + 1]
                R_j += 1
            elif map_arr[R_i][R_j + 1] == 'O':
                return 1, R_i, R_j, B_i, B_j

            if map_arr[B_i][B_j + 1] == '.':
                map_arr[B_i][B_j + 1], map_arr[B_i][B_j] = map_arr[B_i][B_j], map_arr[B_i][B_j + 1]
                B_j += 1
            elif map_arr[B_i][B_j + 1] == 'O':
                return -1, R_i, R_j, B_i, B_j

        return 0, R_i, R_j, B_i, B_j


    #3. direction = up
    if direction == 'up':
        while (R_i - 1 > 0 and (map_arr[R_i - 1][R_j] == '.' or map_arr[R_i - 1][R_j] == 'O')) or (B_i - 1 > 0 and (map_arr[B_i - 1][B_j] == '.' or map_arr[B_i - 1][B_j] == 'O')):
            if map_arr[R_i - 1][R_j] == '.':
                map_arr[R_i - 1][R_j], map_arr[R_i][R_j] = map_arr[R_i][R_j], map_arr[R_i - 1][R_j]
                R_i -= 1
            elif map_arr[R_i - 1][R_j] == 'O':
                return 1, R_i, R_j, B_i, B_j

            if map_arr[B_i - 1][B_j] == '.':
                map_arr[B_i - 1][B_j], map_arr[B_i][B_j] = map_arr[B_i][B_j], map_arr[B_i - 1][B_j]
                B_i -= 1
            elif map_arr[B_i - 1][B_j] == 'O':
                return -1, R_i, R_j, B_i, B_j

        return 0, R_i, R_j, B_i, B_j


    #4. direction = down
    if direction == 'down':
        while (R_i + 1 < n - 1 and (map_arr[R_i + 1][R_j] == '.' or map_arr[R_i + 1][R_j] == 'O')) or (B_i + 1 < n - 1 and (map_arr[B_i + 1][B_j] == '.' or map_arr[B_i + 1][B_j] == 'O')):
            if map_arr[R_i + 1][R_j] == '.':
                map_arr[R_i + 1][R_j], map_arr[R_i][R_j] = map_arr[R_i][R_j], map_arr[R_i + 1][R_j]
                R_i += 1
            elif map_arr[R_i + 1][R_j] == 'O':
                return 1, R_i, R_j, B_i, B_j

            if map_arr[B_i + 1][B_j] == '.':
                map_arr[B_i + 1][B_j], map_arr[B_i][B_j] = map_arr[B_i][B_j], map_arr[B_i + 1][B_j]
                B_i += 1
            elif map_arr[B_i + 1][B_j] == 'O':
                return -1, R_i, R_j, B_i, B_j

        return 0, R_i, R_j, B_i, B_j


    return -1, R_i, R_j, B_i, B_j


nm = input().split()
n = int(nm[0])
m = int(nm[1])

map_arr = [['.'] * m for i in range(n)]

for i in range(n):
    line_input = input()
    for j in range(m):
        map_arr[i][j] = line_input[j]

visit_hash = {}
min_count = [2**31 - 1]
R_i, R_j, B_i, B_j = check_ball_position(map_arr)
check_maze(map_arr, R_i, R_j, B_i, B_j, 0, min_count, visit_hash)

if min_count[0] == 2**31 - 1:
    print(-1)
else:
    print(min_count[0])


#
# for l in range(n):
#     print(map_arr[l])
#
# temp, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'down')
# print('')
# for l in range(n):
#     print(map_arr[l])
# print(temp)
#
# temp, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'right')
# print('')
# for l in range(n):
#     print(map_arr[l])
# print(temp)
#
# temp, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'up')
# print('')
# for l in range(n):
#     print(map_arr[l])
# print(temp)
#
# temp, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'right')
# print('')
# for l in range(n):
#     print(map_arr[l])
# print(temp)
#
# temp, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'down')
# print('')
# for l in range(n):
#     print(map_arr[l])
# print(temp)
#
# temp, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'left')
# print('')
# for l in range(n):
#     print(map_arr[l])
# print(temp)
#
# temp, R_i, R_j, B_i, B_j = move_ball(map_arr, R_i, R_j, B_i, B_j, 'down')
# print('')
# for l in range(n):
#     print(map_arr[l])
# print(temp)
