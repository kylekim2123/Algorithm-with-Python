dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == '0':
            maze[nx][ny] = '1'
            dfs(nx, ny)

for t in range(1, int(input())+1):
    n = int(input())
    maze = []
    for i in range(n):
        line = list(input())
        maze.append(line)
        for j in range(n):
            if line[j] == '2':
                start_x, start_y = i, j
                break
            if line[j] == '3':
                end_x, end_y = i, j
                maze[i][j] = '0'
                break
    dfs(start_x, start_y)
    print('#%s %s' % (t, maze[end_x][end_y]))
