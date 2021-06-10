# 16236. 아기 상어 (골드4)

import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y, *end):
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and baby_size >= area[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                if (nx, ny) == end:
                    return visited[nx][ny] - 1
                queue.append((nx, ny))

n = int(input())
area, fishes = [], []
for i in range(n):
    line = list(map(int, input().split()))
    area.append(line)
    for j in range(n):
        if line[j] == 9:
            bx, by = (i, j)
        elif line[j]:
            fishes.append((i, j))

baby_size, baby_eating, seconds = 2, 0, 0
while True:
    area[bx][by] = 0
    targets = []
    for i, j in fishes:
        if area[i][j] < baby_size:
            distance = bfs(bx, by, i, j)
            if distance:
                targets.append((distance, i , j))
    if not targets:
        break
    targets.sort(key=lambda x: (x[0], x[1], x[2]))
    seconds += targets[0][0]
    bx, by = targets[0][1], targets[0][2]
    fishes.pop(fishes.index((bx, by)))
    baby_eating += 1
    if baby_eating >= baby_size:
        baby_size += 1
        baby_eating = 0
print(seconds)
