# 2468. 안전 영역 (실버1)

import sys
from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] > h and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1

n = int(input())
heights = set()
area = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    area.append(line)
    heights.update(line)

safe = 1
for h in heights:
    visited = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > h and not visited[i][j]:
                bfs(i, j)
                count += 1
    safe = max(safe, count)
print(safe)