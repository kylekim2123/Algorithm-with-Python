# 1953. 탈주범 검거

from collections import deque

direction = {
    '1': ([-1, 1, 0, 0], [0, 0, -1, 1]),
    '2': ([-1, 1], [0, 0]),
    '3': ([0, 0], [-1, 1]),
    '4': ([-1, 0], [0, 1]),
    '5': ([1, 0], [0, 1]),
    '6': ([1, 0], [0, -1]),
    '7': ([-1, 0], [0, -1])
    }

def is_possible_move(x, y, nx, ny):
    dnx, dny = direction[tunnel[nx][ny]]
    for i in range(len(dnx)):
        if x == nx+dnx[i] and y == ny+dny[i]:
            return True
    return False
        
def bfs(x, y):
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if visited[x][y] == l:
            break
        dx, dy = direction[tunnel[x][y]]
        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and tunnel[nx][ny] != '0' and not visited[nx][ny] and is_possible_move(x, y, nx, ny):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return sum(1 for i in range(n) for j in range(m) if visited[i][j])

for t in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [input().split() for _ in range(n)]
    print('#%s %s' % (t, bfs(r, c)))