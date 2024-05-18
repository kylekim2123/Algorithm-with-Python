# 13565. 침투 (실버2)

import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and fiber[nx][ny] == "0"
            ):
                if nx == n - 1:
                    return True
                visited[nx][ny] = True
                queue.append((nx, ny))


n, m = map(int, input().split())
fiber = [input().rstrip() for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(m):
    if fiber[0][i] == "0" and bfs(0, i):
        print("YES")
        break
else:
    print("NO")
