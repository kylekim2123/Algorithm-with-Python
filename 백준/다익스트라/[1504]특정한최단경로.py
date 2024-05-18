# 1504. 특정한 최단 경로 (골드4)

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = [(0, start)]
    distance = [INF] * (n+1)
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for next_node, w in graph[now]:
            next_dist = dist + w
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(queue, (next_dist, next_node))
    return distance

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

_v1= dijkstra(v1)
_v2 = dijkstra(v2)
one = _v1[1] + _v1[v2] + _v2[n]
two = _v2[1] + _v2[v1] + _v1[n]
result = min(one, two)
if result >= INF:
    print(-1)
else:
    print(result)