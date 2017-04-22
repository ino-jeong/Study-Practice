# fail
n = int(input())
line_input = input().split()

block_arr = []
for b in line_input:
    block_arr.append(int(b))

max_height = [0]
memo_arr = [[0] * 250001 for i in range(51)]


def check_tower (cur, higher, diff, max_height):
    print('cur :',cur,'higher :',higher,'diff :',diff,'max_height :',max_height[0])
    if higher > 250000 or cur >= n:
        return

    if diff == 0:
        max_height[0] = max(higher, max_height[0])

    if memo_arr[cur][diff] == 1:
        return



    lower = higher - diff
    new_block = block_arr[cur]

    #1. no use of new block
    check_tower(cur + 1, higher, diff, max_height)

    #2. add new block at higher side
    check_tower(cur + 1, higher + new_block, diff + new_block, max_height)

    #3-1. add new block at lower side. new_block > diff
    if new_block > diff:
        check_tower(cur + 1, lower + new_block, new_block - diff, max_height)
    # 3-2. add new block at lower side. new_block <= diff
    else:
        check_tower(cur + 1, higher, diff - new_block, max_height)

    memo_arr[cur][diff] = 1
    return

check_tower(0, 0, 0, max_height)
if max_height[0] == 0:
    print(-1)
else:
    print(max_height[0])
