# 13565. 침투 (실버2)

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(x, y):
    if x == n - 1:
        return True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and fiber[nx][ny] == "0":
            visited[nx][ny] = True
            if dfs(nx, ny):
                return True
    return False


n, m = map(int, input().split())
fiber = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(m):
    if fiber[0][i] == "0" and not visited[0][i]:
        visited[0][i] = True
        if dfs(0, i):
            print("YES")
            break
else:
    print("NO")
