# 1916. 최소비용 구하기 (골드5)

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, now = heapq.heappop(queue)
        if costs[now] < cost:
            continue
        if now == end:
            return cost
        for next_node, c in cities[now]:
            cost_next = cost + c
            if cost_next < costs[next_node]:
                costs[next_node] = cost_next
                heapq.heappush(queue, (cost_next, next_node))


n, m = int(input()), int(input())
cities = [[] for _ in range(n+1)]
costs = [INF] * (n+1)
for _ in range(m):
    s, e, c = map(int, input().split())
    cities[s].append((e, c))
start, end = map(int, input().split())
print(dijkstra(start, end))
