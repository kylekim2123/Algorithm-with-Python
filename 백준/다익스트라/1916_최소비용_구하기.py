# 골드 5

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 99999999


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)

        if distance[node] < min_dist:
            continue

        if node == end:
            return  # 도착 도시에 대한 최단 경로가 확정 되면 더이상 탐색할 필요 없음

        for next_node, dist in graph[node]:
            next_dist = distance[node] + dist

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))


n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])
