import sys

input = sys.stdin.readline


def dfs(x, y):
    global counts
    counts += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[x][y] == board[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_counts = 0
total = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            counts = 0

            dfs(i, j)

            if counts >= 4:
                total += 1
            max_counts = max(max_counts, counts)

print(total, max_counts)
