# 1795. 인수의 생일 파티

from heapq import heappop, heappush
INF = int(1e9)

def dijkstra(start, graph):
    D = [INF] * (n+1)
    D[start] = 0
    queue = [(0, start)]
    while queue:
        d, now = heappop(queue)
        if D[now] < d:
            continue
        for next_node, w in graph[now]:
            next_d = d + w
            if next_d < D[next_node]:
                D[next_node] = next_d
                heappush(queue, (next_d, next_node))
    return D[1:]

for t in range(1, int(input())+1):
    n, m, x = map(int, input().split())
    graph1, graph2 = [[] for _ in range(n+1)], [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph1[s].append((e, w))
        graph2[e].append((s, w))

    result = max(a+b for a, b in zip(dijkstra(x, graph1), dijkstra(x, graph2)))
    print('#%s %s' % (t, result))