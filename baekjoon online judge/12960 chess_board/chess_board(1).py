# fail...

rc = input().split()
r = int(rc[0])
c = int(rc[1])

board_map = []
for line in range(r):
    board_map.append(input())

d = [[-1] * (2**(2*c + 2) - 1) for i in range(r * c)] #cur position : 'c'


def chess_tiling(cur, state):
    if cur == r * c:
        return 0

    if d[cur][state] != -1:
        return d[cur][state]

    i = int(cur / c)
    j = cur % c

    ans = 0

    if board_map[i][j] == 'X':
        ans = chess_tiling(cur + 1, state >> 1)

    elif state & (1<<c) != 0:
        ans = chess_tiling(cur + 1, state >> 1)

    else:
        ans = chess_tiling(cur + 1, state >> 1)
        if (i + j) % 2 != 0:
            ans = chess_tiling(cur + 1, state >> 1)
        else:
            pass
            # 1. tile type-A '⌊'
            result_state = tile_check(i, j, state, 'A')
            if result_state != 0:
                ans = chess_tiling(cur + 2, result_state >> 2) + 1

            # 2. tile type-B '⌈'
            result_state = tile_check(i, j, state, 'B')
            if result_state != 0:
                ans = max(ans, chess_tiling(cur + 2, result_state >> 2) + 1)

            # 3. tile type-C '⌉'
            result_state = tile_check(i, j, state, 'C')
            if result_state != 0:
                ans = max(ans, chess_tiling(cur + 1, result_state >> 1) + 1)

            # 4. tile type-D '⌋'
            result_state = tile_check(i, j, state, 'D')
            if result_state != 0:
                ans = max(ans, chess_tiling(cur + 1, result_state >> 1) + 1)

    d[cur][state] = ans
    return ans



def tile_check(i, j, state, type):  # return result state if certain type of tile can be assigned
    result_state = 0

    # 1. tile type-A '⌊'
    if type == 'A':
        if i > 0 and j < (c - 1) and board_map[i - 1][j] == '.' and board_map[i][j + 1] == '.':
            if state & 1 == 0 and state & (1 << (c+1)) == 0:
                result_state = state | 1 | (1 << (c+1)) | 1 << c
                return result_state

    # 2. tile type-B '⌈'
    elif type == 'B':
        if i < (r - 1) and j < (c - 1) and board_map[i + 1][j] == '.' and board_map[i][j + 1] == '.':
            if state & (2*c) == 0 and state & (1 << (c+1)) == 0:
                result_state = state | (1 << (2*c)) | (1 << (c+1)) | 1 << c
                return result_state

    # 3. tile type-C '⌉'
    elif type == 'C':
        if i < (r - 1) and j > 0 and board_map[i + 1][j] == '.' and board_map[i][j - 1] == '.':
            if state & (2*c) == 0 and state & (1 << (c-1)) == 0:
                result_state = state | (1 << (2*c)) | (1 << (c-1)) | 1 << c
                return result_state

    # 4. tile type-D '⌋'
    elif type == 'D':
        if i > 0 and j > 0 and board_map[i - 1][j] == '.' and board_map[i][j - 1] == '.':
            if state & 1 == 0 and state & (1 << (c-1)) == 0:
                result_state = state | 1 | (1 << (c-1)) | 1 << c
                return result_state

    return result_state

print(chess_tiling(0, 0))

