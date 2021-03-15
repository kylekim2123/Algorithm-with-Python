# 2217. 홈 방범 서비스

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y, k):
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    queue = deque([(x, y)])
    house = 0
    if city[x][y]:
        house += 1
    while queue:
        x, y = queue.popleft()
        if visited[x][y] >= k:
            return house
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                if city[nx][ny]:
                    house += 1
    return house

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    result = {0}
    size = 1
    while size <= 25:
        for i in range(n):
            for j in range(n):
                house = bfs(i, j, size)
                benefit = (house*m) - (size*size+(size-1)*(size-1))
                if benefit >= 0:
                    result.add(house)
        size += 1
    print('#%s %s' % (t, max(result)))
    