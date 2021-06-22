# 2665. 미로 만들기 (골드4)

import sys
from heapq import heappop, heappush
input = sys.stdin. readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
INF = int(1e9)

def dijkstra(x, y):
    distance = [[INF]*n for _ in range(n)]
    distance[x][y] = 0
    queue = [(0, x, y)]
    while queue:
        dist, x, y = heappop(queue)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_dist = distance[x][y]
                if rooms[nx][ny] == '0':
                    next_dist += 1
                if next_dist < distance[nx][ny]:
                    distance[nx][ny] = next_dist
                    heappush(queue, (next_dist, nx, ny))
    return distance[-1][-1]

n = int(input())
rooms = [input().rstrip() for _ in range(n)]
print(dijkstra(0, 0))
