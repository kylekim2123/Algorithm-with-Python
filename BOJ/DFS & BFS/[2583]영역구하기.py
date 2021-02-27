# 2583. 영역 구하기 (실버1)

import sys
sys.setrecursionlimit(10000)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global surface
    surface += 1
    area[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not area[nx][ny]:
            dfs(nx, ny)

m, n, k = map(int, input().split())
area = [[0]*n for _ in range(m)]
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            area[i][j] = 1
count = 0
surfaces = []
for i in range(m):
    for j in range(n):
        if not area[i][j]:
            surface = 0
            count += 1
            dfs(i, j)
            surfaces.append(surface)
print(count)
print(*sorted(surfaces))