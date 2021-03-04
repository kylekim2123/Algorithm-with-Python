# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    queue = [(x, y)]
    visited[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != '1':
                visited[nx][ny] = visited[x][y] + 1
                if maze[nx][ny] == '3':
                    return visited[nx][ny] - 2
                queue.append((nx, ny))
    return 0

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
    print('#%s %s' % (t, bfs(start_x, start_y)))
