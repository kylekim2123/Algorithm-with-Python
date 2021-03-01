# 3184. 양 (실버2)

import sys
from collections import deque
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    sheep, wolf = 0, 0
    queue = deque([(x, y)])
    if farm[x][y] == 'v':
        wolf += 1
    elif farm[x][y] == 'o':
        sheep += 1
    farm[x][y] = '#'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and farm[nx][ny] != '#':
                if farm[nx][ny] == 'v':
                    wolf += 1
                elif farm[nx][ny] == 'o':
                    sheep += 1
                farm[nx][ny] = '#'
                queue.append((nx, ny))
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf

r, c = map(int, input().split())
farm = [list(input().rstrip()) for _ in range(r)]
alive_sheep, alive_wolf = 0, 0
for i in range(r):
    for j in range(c):
        if farm[i][j] != '#':
            sheep, wolf = bfs(i, j)
            alive_sheep += sheep
            alive_wolf += wolf
print(alive_sheep, alive_wolf)