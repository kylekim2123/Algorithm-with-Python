# 3187. 양치기 꿍 (실버2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    global sheep, wolf
    if field[x][y] == 'v':
        wolf += 1
    elif field[x][y] == 'k':
        sheep += 1
    field[x][y] = '#'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and field[nx][ny] != '#':
            dfs(nx, ny)

r, c = map(int, input().split())
field = [list(input().rstrip()) for _ in range(r)]
t_sheep, t_wolf = 0, 0
for i in range(r):
    for j in range(c):
        if field[i][j] == 'v' or field[i][j] == 'k':
            sheep, wolf = 0, 0
            dfs(i, j)
            if sheep > wolf:
                t_sheep += sheep
            else:
                t_wolf += wolf
print(t_sheep, t_wolf)