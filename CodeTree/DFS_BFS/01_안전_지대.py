import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] > 0:
                temp[nx][ny] = 0
                queue.append((nx, ny))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_k = 1
max_safe_area = 0

for k in range(1, 101):
    temp = [[0 if house <= k else house for house in line] for line in board]
    safe_area = 0

    for i in range(n):
        for j in range(m):
            if temp[i][j] > 0:
                temp[i][j] = 0
                bfs(i, j)
                safe_area += 1

    if safe_area > max_safe_area:
        max_k = k
        max_safe_area = safe_area

print(max_k, max_safe_area)
