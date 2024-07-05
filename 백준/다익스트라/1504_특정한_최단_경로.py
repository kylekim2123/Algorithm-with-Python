# 골드 4

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 9999999


def dijkstra(start):
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


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

# 이전 다익스트라 문제와 다르게, 출발 정점에서 최단 경로를 찾지 않는다.
# 반드시 지나야 하는 두 정점에서 각각 다익스트라를 통해 다른 정점으로의 최단 경로를 찾는다.
v1, v2 = map(int, input().split())  # 반드시 지나야 하는 두 정점
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

# (1 -> v1 -> v2 -> n) 혹은 (1 -> v2 -> v1 -> n) 중 더 짧은 경로를 선택한다.
v1_first_dist = v1_distance[1] + v1_distance[v2] + v2_distance[n]
v2_first_dist = v2_distance[1] + v2_distance[v1] + v1_distance[n]
result = min(v1_first_dist, v2_first_dist)

if result >= INF:
    print(-1)  # v1, v2를 반드시 거치는 경로가 없으면, -1을 출력
else:
    print(result)
