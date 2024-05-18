# 골드 5

import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(x):
    distance[x] = 0
    heap = [(0, x)]

    while heap:
        min_dist, x = heappop(heap)

        if min_dist > distance[x]:
            continue

        for i in range(3):
            if dx[i] == 2:
                nx = x * 2
                next_dist = min_dist
            else:
                nx = x + dx[i]
                next_dist = min_dist + 1

            if 0 <= nx <= 100000 and next_dist < distance[nx]:
                distance[nx] = next_dist
                heappush(heap, (next_dist, nx))


n, k = map(int, input().split())
distance = [9999999] * 100001
dx = [-1, 1, 2]

dijkstra(n)

print(distance[k])
