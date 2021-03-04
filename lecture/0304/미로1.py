# 상 하 좌 우
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def find_start_point():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                return i, j

def bfs(x, y):
    queue = [(x, y)]
    maze[x][y] = '1'
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if maze[nx][ny] != '1':
                if maze[nx][ny] == '3':
                    return 1
                queue.append((nx, ny))
                maze[nx][ny] = '1'
    return 0

for _ in range(1, 11):
    t = input()
    maze = [list(input()) for _ in range(16)]
    start_x, start_y = find_start_point()
    print('#%s %s' % (t, bfs(start_x, start_y)))
