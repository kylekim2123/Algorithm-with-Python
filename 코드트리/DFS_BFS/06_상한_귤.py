import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
board = []
queue = deque()
visited = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for x in range(n):
    line = list(map(int, input().split()))
    board.append(line)

    for y in range(n):
        if line[y] == 0:
            visited[x][y] = -1
        elif line[y] == 2:
            queue.append((x, y))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            board[nx][ny] = 2
            queue.append((nx, ny))

for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            visited[x][y] = -2

for line in visited:
    print(*line)
