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
maze_queue.append((0, 0))  # (y,x)

check = [[False] * 100 for i in range(100)]
check[0][0] = True

dist = [[0] * 100 for i in range(100)]
dist[0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while len(maze_queue) >= 0:
    y, x = maze_queue.pop(0)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < n and 0 <= ny < m:
            if maze[ny][nx] == 1 and check[ny][nx] == False:
                dist[ny][nx] = dist[y][x] + 1
                check[ny][nx] = True
                maze_queue.append((ny, nx))

print(dist[m-1][n-1])
for maze_line in maze:
    print(maze_line)
