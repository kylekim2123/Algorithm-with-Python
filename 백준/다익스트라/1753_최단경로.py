# 골드 4

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 9999999


def dijkstra(start):
    distance[start] = 0  # 출발 정점 방문
    heap = [(0, start)]

    while heap:
        min_dist, node = heappop(heap)  # 갈 수 있는 정점 중 가장 최단 경로의 정점을 선택

        if distance[node] < min_dist:
            continue  # 그런데 이미 최단 경로로 기록된 값보다 큰 경우, 탐색할 필요가 없음

        for next_node, dist in graph[node]:  # 해당 정점과 인접한 다음 정점들에 대해
            next_dist = min_dist + dist  # 다음 정점까지의 거리를 계산하고

            if next_dist < distance[next_node]:  # 다음 정점에 기록된 최단 경로보다 더 짧은 경우
                distance[next_node] = next_dist  # 다음 정점의 최단 경로를 갱신
                heappush(heap, (next_dist, next_node))  # 탐색을 해야 하므로 힙에 삽입


n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(start)

for node in range(1, n + 1):
    if distance[node] == INF:
        print("INF")
    else:
        print(distance[node])
