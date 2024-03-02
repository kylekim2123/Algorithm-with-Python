# 골드 2

import sys

input = sys.stdin.readline
EMPTY, BUILDING = ".", "x"


def dfs(x, y):
    for i in range(3):
        nx, ny = x + dx[i], y + 1
        if 0 <= nx < n and board[nx][ny] == EMPTY and not visited[nx][ny]:
            visited[nx][ny] = True

            if ny == m - 1 or dfs(nx, ny):
                return True

    return False


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1]
total = 0

for x in range(n):
    if not visited[x][0]:
        visited[x][0] = True

        if dfs(x, 0):
            total += 1

print(total)
