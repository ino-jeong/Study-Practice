def cal(count, sum, goal):
    if count > 10:
        return 0

    if sum > goal:
        return  0

    if sum == goal:
        return 1

    now = 0
    for i in range(1,4):
        now += cal(count + 1, sum + i, goal)

    return now

cases = int(input())
for c in range(cases):
    n = int(input())
    print(cal(0, 0, n))
