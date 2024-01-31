# 골드 1

import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    queue = deque([(x, y)])
    pool = [(x, y)]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[x][y] >= land[nx][ny]:
                if nx == 0 or ny == 0 or nx == n - 1 or ny == m - 1:
                    return 0

                visited[nx][ny] = True
                queue.append((nx, ny))
                pool.append((nx, ny))

    for x, y in pool:
        land[x][y] += 1

    return len(pool)


n, m = map(int, input().split())
land = [list(map(int, input().rstrip())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
total = 0

for i in range(1, max(map(max, land))):
    for x in range(1, n - 1):
        for y in range(1, m - 1):
            if land[x][y] == i:
                total += bfs(x, y)

print(total)
