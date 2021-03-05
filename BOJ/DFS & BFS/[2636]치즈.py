# 2636. 치즈 (골드5)

from collections import deque
import sys
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_outside_air(x, y):
    queue = deque([(x, y)])
    cheese[x][y] = 2
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and cheese[nx][ny] == 0:
                cheese[nx][ny] = 2
                queue.append((nx, ny))

def melt_cheese():
    melting = [[0]*m for _ in range(n)]
    count = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if cheese[i][j] == 1:
                count += 1
                for k in range(4):
                    ni, nj = i+dx[k], j+dy[k]
                    if not melting[i][j] and cheese[ni][nj] == 2:
                        melting[i][j] = 1
    is_all_melted = True
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 2:
                cheese[i][j] = 0
            cheese[i][j] -= melting[i][j]
            if cheese[i][j] == 1:
                is_all_melted = False
    return is_all_melted, count


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
hour, all_melted = 0, False
while not all_melted:
    bfs_outside_air(0, 0)
    all_melted, last_count = melt_cheese()
    hour += 1
print(hour, last_count, sep='\n')
