# 2636. 치즈 (골드5)

from collections import deque
import sys
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt():
    is_all_melted = True
    count = 0
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 2:
                cheese[i][j] = 0
            cheese[i][j] -= melting[i][j]
            if cheese[i][j] == 1:
                count += 1
                is_all_melted = False
    return is_all_melted, count

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

# 이 부분을 고쳐보자. 치즈 부분은 bfs로 하지 않아도 될거 같다. 그냥 for문으로만 돌아도 되지 않을까?
# 그리고 melt()와 합칠 수 있지 않을까?
def bfs_cheese(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not melting[x][y] and cheese[nx][ny] == 2:
                melting[x][y] = 1
            if not visited[nx][ny] and cheese[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

n, m = map(int, input().split())
cheese = []
last_count = 0
for i in range(n):
    line = list(map(int, input().split()))
    cheese.append(line)
    last_count += line.count(1)
hour, all_melted = 0, False
while not all_melted:
    bfs_outside_air(0, 0)
    visited = [[False]*m for _ in range(n)]
    melting = [[0]*m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and cheese[i][j] == 1:
                bfs_cheese(i, j)
    temp = last_count
    all_melted, last_count = melt()
    hour += 1
    if last_count == 0:
        last_count = temp
print(hour, last_count, sep='\n')
