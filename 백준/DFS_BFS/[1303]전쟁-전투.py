# 1303. 전쟁-전투 (실버1)

import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우


def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (
            0 <= nx < n
            and 0 <= ny < m
            and not visited[nx][ny]
            and board[x][y] == board[nx][ny]
        ):
            global total
            total += 1
            visited[nx][ny] = True
            dfs(nx, ny)


def bfs(x, y):
    total = 1
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and board[x][y] == board[nx][ny]
            ):
                total += 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    return total


m, n = map(int, input().split())
board = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = {"W": 0, "B": 0}

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            total = 1
            dfs(i, j)
            # total = bfs(i, j)
            result[board[i][j]] += total ** 2

print(result["W"], result["B"])
