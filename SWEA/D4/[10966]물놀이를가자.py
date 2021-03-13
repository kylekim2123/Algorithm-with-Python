# 10966. 물놀이를 가자

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    queue, grid = deque(), []
    for i in range(n):
        line = input()
        grid.append(line)
        for j in range(m):
            if line[j] == 'W':
                queue.append((i, j))

    total = 0
    visited = [[0]*m for _ in range(n)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                total += visited[nx][ny]
                queue.append((nx, ny))
    print(f'#{t} {total}')