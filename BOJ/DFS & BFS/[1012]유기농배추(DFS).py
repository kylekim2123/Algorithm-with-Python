# 1012. 유기농 배추 (실버 2) - DFS

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
            field[nx][ny] = 0
            dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    total = 0

    for _ in range(k):
        y, x = map(int, input().split())
        field[x][y] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                field[i][j] = 0
                dfs(i, j)
                total += 1

    print(total)
