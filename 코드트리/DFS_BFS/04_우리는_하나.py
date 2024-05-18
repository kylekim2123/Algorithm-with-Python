import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, k, u, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
locations = [(i, j) for i in range(n) for j in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_cities = k

for case in combinations(locations, k):
    visited = [[False] * n for _ in range(n)]
    queue = deque(case)
    cities = k

    for x, y in queue:
        visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and u <= abs(board[x][y] - board[nx][ny]) <= d:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cities += 1

    max_cities = max(max_cities, cities)

print(max_cities)
