def cal_cost(cost_map, cost_hash, left, right, n):
    if (left, right) in cost_hash:
        return cost_hash[(left, right)]

    next_num = max(left, right) + 1

    if next_num == n:
        return 0

    cost_hash[(left, right)] = min(cost_map[next_num][left] + cal_cost(cost_map, cost_hash, next_num, right, n),
                                   cost_map[right][next_num] + cal_cost(cost_map, cost_hash, left, next_num, n))

    return cost_hash[(left, right)]


n = int(input())
cost_map = [[0] * n for i in range(n)]
cost_hash = {}

for i in range(n):
    line_input = input().split()
    for j in range(n):
        cost_map[i][j] = int(line_input[j])

print(cal_cost(cost_map, cost_hash, 0,0, n))
