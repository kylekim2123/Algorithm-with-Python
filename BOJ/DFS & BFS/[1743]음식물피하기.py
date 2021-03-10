# 1743. 음식물 피하기 (실버1)

import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    passage[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and passage[nx][ny]:
                global area
                area += 1
                passage[nx][ny] = 0
                queue.append((nx, ny))

n, m, k = map(int, input().split())
passage = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    passage[r-1][c-1] = 1

max_area = 0
for i in range(n):
    for j in range(m):
        if passage[i][j]:
            area = 1
            bfs(i, j)
            max_area = max(max_area, area)
print(max_area)