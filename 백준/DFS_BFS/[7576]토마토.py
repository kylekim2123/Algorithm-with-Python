# 7576. 토마토 (골드5)

import sys
from collections import deque

input = sys.stdin.readline


def is_ripe():
    for line in box:
        for tomato in line:
            if tomato == 0:
                return False
    return True


m, n = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
box, queue = [], deque()

for i in range(n):
    line = list(map(int, input().split()))
    box.append(line)
    for j in range(m):
        if line[j] == 1:
            queue.append((i, j, 0))

# bfs
while queue:
    x, y, day = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = 1
            queue.append((nx, ny, day + 1))

if not is_ripe():
    print(-1)
else:
    print(day)
