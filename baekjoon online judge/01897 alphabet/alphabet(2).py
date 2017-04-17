def calc_dist(map_arr, r, c, cur_pos, cur_dist, visit_str):
    i = cur_pos[0]
    j = cur_pos[1]
    # print('*** current char :', map_arr[i][j])

    ch = map_arr[i][j]
    visit_str += ch

    cur_dist += 1
    dist = cur_dist

    # left
    if j-1 >= 0:
        next_chr = map_arr[i][j-1]
        if check_visit(next_chr, visit_str):
            # print('*** left')
            dist = max(dist, calc_dist(map_arr, r, c, (i, j-1), cur_dist, visit_str))

    # right
    if j+1 < c:
        next_chr = map_arr[i][j+1]
        if check_visit(next_chr, visit_str):
            # print('*** right')
            dist = max(dist, calc_dist(map_arr, r, c, (i, j+1), cur_dist, visit_str))

    # up
    if i-1 >= 0:
        next_chr = map_arr[i-1][j]
        if check_visit(next_chr, visit_str):
            # print('*** up')
            dist = max(dist, calc_dist(map_arr, r, c, (i-1, j), cur_dist, visit_str))

    # down
    if i+1 < r:
        next_chr = map_arr[i+1][j]
        if check_visit(next_chr, visit_str):
            # print('*** down')
            dist = max(dist, calc_dist(map_arr, r, c, (i+1, j), cur_dist, visit_str))

    return dist

def check_visit(next_chr, visit_str):
    return next_chr not in visit_str

rc = input().split()

r = int(rc[0])
c = int(rc[1])

map_arr = [['0'] * c for i in range(r)]
for i in range(r):
    line_input = input()
    for j in range(c):
        map_arr[i][j] = line_input[j]

visit_str = ''

# for line in map_arr:
#     print(line)

result = calc_dist(map_arr, r, c, (0,0), 0, visit_str)
print(result)

