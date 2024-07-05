# 골드 2

import sys
from heapq import heappop, heappush

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


for _ in range(int(input())):
    n, m, t = map(int, input().split())  # 정점, 간선, 목적지 개수
    s, g, h = map(int, input().split())  # 출발지, 교차로1, 교차로2
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    ends = [int(input()) for _ in range(t)]  # 목적지 후보들
    result = []

    s_distance = dijkstra(s)
    g_distance = dijkstra(g)
    h_distance = dijkstra(h)

    # (출발지 -> g -> h -> 목적지) 경로의 비용이 (출발지 -> 목적지) 경로의 최소 비용과 같거나
    # (출발지 -> h -> g -> 목적지) 경로의 비용이 (출발지 -> 목적지) 경로의 최소 비용과 같다면
    # 해당 목적지는 가능한 목적지이다.
    for end in ends:
        s_g_h_end = s_distance[g] + g_distance[h] + h_distance[end]
        s_h_g_end = s_distance[h] + h_distance[g] + g_distance[end]

        if s_g_h_end == s_distance[end] or s_h_g_end == s_distance[end]:
            result.append(end)

    print(*sorted(result))
