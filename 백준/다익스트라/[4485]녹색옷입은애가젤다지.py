# 4485. 녹색 옷 입은 애가 젤다지? (골드4)

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y):
    distance = [[INF]*n for _ in range(n)]
    distance[x][y] = maze[x][y]
    queue = [(maze[x][y], x, y)]
    while queue:
        dist, x, y = heapq.heappop(queue)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                n_dist = dist + maze[nx][ny]
                if n_dist < distance[nx][ny]:
                    distance[nx][ny] = n_dist
                    heapq.heappush(queue, (n_dist, nx, ny))
    return distance[-1][-1]


t = 1
while True:
    n = int(input())
    if not n:
        break
    maze = [list(map(int, input().split())) for _ in range(n)]
    print(f'Problem {t}: {bfs(0, 0)}')
    t += 1
    