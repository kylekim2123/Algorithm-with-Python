INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        dist, now = queue.pop(0)
        if distance[now] < dist:
            continue
        if now == n:
            return dist
        for next_node, w in graph[now]:
            next_dist = dist + w
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                queue.append((next_dist, next_node))
        queue.sort()


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    print('#%s %s' % (t, dijkstra(0)))