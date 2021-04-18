# 1238. 파티 (골드3)

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, graph):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for next_node, t in graph[now]:
            next_t = dist + t
            if next_t < distance[next_node]:
                distance[next_node] = next_t
                heapq.heappush(queue, (next_t, next_node))
    return distance


n, m, x = map(int, input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph1[s].append((e, t))
    graph2[e].append((s, t))

max_time = 0
departure = dijkstra(x, graph2)
destination = dijkstra(x, graph1)
for i in range(1, n+1):
    max_time = max(max_time, departure[i]+destination[i])
print(max_time)