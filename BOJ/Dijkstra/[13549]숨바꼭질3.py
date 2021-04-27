# 13549. 숨바꼭질3 (골드5)

import sys
from collections import deque
input = sys.stdin.readline
INF = 100001
dx = [2, 1, -1]

def dijkstra(start):
    visited = [False] * INF
    visited[start] = True
    distance = [INF] * INF
    distance[start] = 0
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == k:
            return distance[x]
        for i in range(3):
            if dx[i] == 2 and x:
                nx = x+x
                if nx < INF and not visited[nx]:
                    visited[nx] = True
                    distance[nx] = distance[x]
                    queue.appendleft(nx)
            else:
                nx = x+dx[i]
                if 0 <= nx < INF and not visited[nx]:
                    visited[nx] = True
                    distance[nx] = distance[x] + 1
                    queue.append(nx)


n, k = map(int, input().split())
if n >= k:
    print(n-k)
else:
    print(dijkstra(n))
