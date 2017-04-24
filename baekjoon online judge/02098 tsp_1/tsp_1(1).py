# failed

n = int(input())
cost_arr = [[0] * n for i in range(n)]

for i in range(n):
    line_input = input().split()
    for j in range(n):
        cost_arr[i][j] = int(line_input[j])

visited_arr = [0] * n
visited_arr[0] = 1

memo = [[-1] * (17) for i in range(17)]

def travel_cities(i, count):

    if memo[i][count] != -1:
        return memo[i][count]

    min_cost = 2 ** 31 - 1

    for j in range(n):
        if visited_arr[j] == 0 and cost_arr[i][j] != 0:
            if count == n - 1:
                return cost_arr[i][j] + cost_arr[j][0]
            visited_arr[j] = 1
            min_cost = min(min_cost, cost_arr[i][j] + travel_cities(j, count + 1))
            visited_arr[j] = 0

    memo[i][count] = min_cost
    return min_cost

print(travel_cities(0, 1))

