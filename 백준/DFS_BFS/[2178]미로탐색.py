# 2178. 미로탐색 (실버1)

import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0]*m for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                if nx == n-1 and ny == m-1:
                    return visited[nx][ny]
                queue.append((nx, ny))
                maze[nx][ny] = '0'

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
print(bfs(0, 0))
