# 골드 3

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 9999999


def dijkstra(start, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        if distance[min_node] < min_dist:
            continue

        for next_node, dist in graph[min_node]:
            next_dist = min_dist + dist

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))

    return distance


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # x -> home
reversed_graph = [[] for _ in range(n + 1)]  # home -> x

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    reversed_graph[e].append((s, w))

home_to_x = dijkstra(x, reversed_graph)  # 방향을 반대로 바꾼 그래프는, 각 정점에서 x까지의 최단경로를 알 수 있게 함
x_to_home = dijkstra(x, graph)
result = max(x_to_home[node] + home_to_x[node] for node in range(1, n + 1))

print(result)
