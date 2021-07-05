# 17144. 미세먼지 안녕! (골드5)

import sys
from collections import deque
input = sys.stdin.readline
DX, DY = [-1, 1, 0, 0], [0, 0, -1, 1]


# 미세먼지 확산
def diffuse(dusts):
    queue = deque(dusts)
    while queue:
        x, y = queue.popleft()
        count = 0
        for i in range(4):
            nx, ny = x+DX[i], y+DY[i]
            if 0 <= nx < r and 0 <= ny < c and house[nx][ny] != -1:
                house[nx][ny] += (house[x][y] // 5)
                count += 1
        house[x][y] -= (house[x][y]//5) * count


# 공기청정기 작동
def purify(house):
    prev_dust = 0
    count = (up * c) - 2
    px, py = up, 1
    tx, ty = up, 2
    moving = [(0, 1), (-1, 0), (0, -1), (1, 0)] # 우, 상, 좌, 하
    direction = 0
    while count >= 0:
        house[px][py] = prev_dust
        prev_dust = house[tx][ty]
        dx, dy = moving[direction]


r, c, t = map(int, input().split())
house = []
up, down = -1, -1 # 위쪽, 아래쪽 공기청정기의 행 번호
for i in range(r):
    line = list(map(int, input().split()))
    house.append(line)
    for j in range(c):
        if line[j] == -1 and up < 0:
            up, down = i, i+1

for _ in range(t):
    dusts = [(i, j) for i in range(r) for j in range(c) if house[i][j] > 0]
    diffuse(dusts)
    purify(house)
