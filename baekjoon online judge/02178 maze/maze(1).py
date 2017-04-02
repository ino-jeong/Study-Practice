def possible_way_enqueue(cur, step, maze, maze_queue, m, n):

    (y, x) = cur

    #right
    if x + 1 <= m - 1:
        if maze[y][x+1] == 1:
            right = (y, x + 1)
            maze_queue.append((right, step + 1))
            maze[y][x+1] = 2

    # downside
    if (y + 1 <= n - 1):
        if maze[y + 1][x] == 1:
            down = (y + 1, x)
            maze_queue.append((down, step + 1))
            maze[y + 1][x] = 2

    #upside
    if 0 <= y - 1:
        if maze[y-1][x] == 1:
            up = (y - 1, x)
            maze_queue.append((up, step + 1))
            maze[y - 1][x] =2

    #left
    if 0 <= x - 1:
        if maze[y][x-1] == 1:
            left = (y, x - 1)
            maze_queue.append((left, step + 1))
            maze[y][x - 1] = 2

line_input = input()
line_input = line_input.split(' ')

n = int(line_input[0])
m = int(line_input[1])

maze = []
for line in range(n):
    line_input = input()
    row = []
    for digit in line_input:
        row.append(int(digit))
    maze.append(row)


maze_queue = []
cur = (0,0)
maze_queue.append((cur, 1))  # (y,x),step
maze[0][0] = 2

while cur != (n - 1, m - 1):
    cur, step = maze_queue.pop(0)
    (y,x) = cur
    # maze[y][x] = 2  # check as visited
    # print(step)
    # for maze_line in maze:
    #     print(maze_line)
    possible_way_enqueue(cur, step, maze, maze_queue, m, n)


print(step)
for maze_line in maze:
    print(maze_line)