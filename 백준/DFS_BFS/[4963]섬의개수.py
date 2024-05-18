# 4963. 섬의 개수 (실버2)

import sys

# 좌상 상 우상 우 우하 하 좌하 좌
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if not visited[x][y]:
            visited[x][y] = 1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and square[nx][ny] and not visited[nx][ny]:
                    stack.append((nx, ny))

result = []
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    square = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    
    count = 0
    for i in range(h):
        for j in range(w):
            if square[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1
    result.append(count)
print('\n'.join(map(str, result)))