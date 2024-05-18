# 1926. 그림 (실버1)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and paper[nx][ny]:
            global area
            area += 1
            paper[nx][ny] = 0
            dfs(nx, ny)

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
count, max_area = 0, 0
for i in range(n):
    for j in range(m):
        if paper[i][j]:
            area = 1
            paper[i][j] = 0
            dfs(i, j)
            count += 1
            max_area = max(max_area, area)
print(count, max_area, sep='\n')
