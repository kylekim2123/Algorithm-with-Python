INF = int(1e9)

def dijkstra(start):
    D = [INF] * (n+1)
    D[start] = 0
    queue = [start]
    rp = 0
    while rp < len(queue):
        node = queue[rp]
        rp += 1
        for n_node, w in graph[node]:
            d = D[node] + w
            if d < D[n_node]:
                D[n_node] = d
                queue.append(n_node)
    return D[-1]

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    print('#%s %s' % (t, dijkstra(0)))