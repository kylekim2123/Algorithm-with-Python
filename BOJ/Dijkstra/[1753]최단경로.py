# 1753. 최단경로 (골드5)

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for next_node, w in graph[now]:
            cost = dist + w
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
