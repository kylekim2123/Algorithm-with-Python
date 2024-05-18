# 3055. 탈출 (골드5)

import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(start):
    queue = deque()
    for wx, wy in water:
        queue.append((wx, wy, 'water'))
    i, j = start
    visited = [[0]*c for _ in range(r)]
    visited[i][j] = 1
    queue.append((i, j, 'hedgehog'))
    while queue:
        x, y, mark = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if mark == 'water' and forest[nx][ny] in {'.', 'S'}:
                    forest[nx][ny] = '*'
                    queue.append((nx, ny, 'water'))
                elif mark == 'hedgehog' and not visited[nx][ny] and forest[nx][ny] in {'.', 'D'}:
                    visited[nx][ny] = visited[x][y] + 1
                    if forest[nx][ny] == 'D':
                        return visited[x][y]
                    queue.append((nx, ny, 'hedgehog'))
    return 'KAKTUS'


r, c = map(int, input().split())
forest, water = [], []
for i in range(r):
    line = list(input())
    forest.append(line)
    for j in range(c):
        if line[j] == 'S':
            hedgehog = (i, j)
        elif line[j] == '*':
            water.append((i, j))
print(bfs(hedgehog))