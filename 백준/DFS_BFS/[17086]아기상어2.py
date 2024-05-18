# 17086. 아기상어2 (실버2)

import sys
from collections import deque

input = sys.stdin.readline


def bfs(queue):
    max_distance = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
                area[nx][ny] = area[x][y] + 1
                queue.append((nx, ny))
                max_distance = max(max_distance, area[nx][ny])
    return max_distance


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
sharks = deque([(i, j) for i in range(n) for j in range(m) if area[i][j] == 1])

print(bfs(sharks) - 1)
