def calc_dist(map_arr, r, c, cur_pos, cur_dist, visit_list):
    i = cur_pos[0]
    j = cur_pos[1]
    print('*** current char :', map_arr[i][j])

    ch = map_arr[i][j]
    visit_list[ord(ch) - ord('A')] = 1

    cur_dist += 1
    dist = cur_dist

    # left
    if j-1 >= 0 and visit_list[ord(map_arr[i][j-1]) - ord('A')] == 0:
        print('*** left')
        dist = max(dist, calc_dist(map_arr, r, c, (i, j-1), cur_dist, visit_list))

    # right
    if j+1 < c and visit_list[ord(map_arr[i][j+1]) - ord('A')] == 0:
        print('*** right')
        dist = max(dist, calc_dist(map_arr, r, c, (i, j+1), cur_dist, visit_list))

    # up
    if i-1 >= 0 and visit_list[ord(map_arr[i-1][j]) - ord('A')] == 0:
        print('*** up')
        dist = max(dist, calc_dist(map_arr, r, c, (i-1, j), cur_dist, visit_list))

    # down
    if i+1 < r and visit_list[ord(map_arr[i+1][j]) - ord('A')] == 0:
        print('*** down')
        dist = max(dist, calc_dist(map_arr, r, c, (i+1, j), cur_dist, visit_list))

    visit_list[ord(ch) - ord('A')] = 0
    return dist


rc = input().split()

r = int(rc[0])
c = int(rc[1])

map_arr = [['0'] * c for i in range(r)]
for i in range(r):
    line_input = input()
    for j in range(c):
        map_arr[i][j] = line_input[j]

visit_list = [0] * 26

for line in map_arr:
    print(line)

result = calc_dist(map_arr, r, c, (0,0), 0, visit_list)
print(result)

