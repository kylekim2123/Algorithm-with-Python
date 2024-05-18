# 10282. 해킹 (골드4)

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        dist, node = heappop(queue)
        if distance[node] < dist:
            continue
        for next_node, w in computers[node]:
            next_dist = dist + w
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(queue, (next_dist, next_node))
    return distance


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    computers = [[] for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        computers[b].append((a, s))
    
    infested_times = dijkstra(c)
    counts, max_time = 0, 0
    for time in infested_times:
        if time < INF:
            counts += 1
            if time > max_time:
                max_time = time
    print(counts, max_time)
    
