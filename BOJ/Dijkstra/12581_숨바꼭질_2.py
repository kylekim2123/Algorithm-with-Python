# 골드 4

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF, LENGTH = 9999999, 100000


def dijkstra(x):
    distance[x] = 0
    heap = [(0, x)]

    while heap:
        min_dist, x = heappop(heap)

        if min_dist > distance[x]:
            continue

        for i in range(3):
            nx = x * 2 if dx[i] == 2 else x + dx[i]
            next_dist = min_dist + 1

            if 0 <= nx <= LENGTH and next_dist <= distance[nx]:
                distance[nx] = next_dist
                heappush(heap, (next_dist, nx))

                if nx == k:
                    counts[next_dist] += 1


n, k = map(int, input().split())
distance = [INF] * (LENGTH + 1)
counts = [0] * INF
dx = [-1, 1, 2]

dijkstra(n)

print(distance[k])
print(counts[distance[k]] if counts[distance[k]] > 0 else 1)
