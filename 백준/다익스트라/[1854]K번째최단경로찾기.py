# 1854. K번째 최단경로 찾기 (플래티넘5)

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = [(0, start)]
    result = [[INF]*k for _ in range(n+1)]
    result[start][0] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        for next_node, w in graph[now]:
            next_dist = dist + w
            if result[next_node][k-1] > next_dist:
                result[next_node][k-1] = next_dist
                result[next_node].sort()
                heapq.heappush(queue, (next_dist, next_node))
    return result

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for res in dijkstra(1)[1:]:
    if res[k-1] >= INF:
        print(-1)
        continue
    print(res[k-1])