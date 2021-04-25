import heapq
INF = int(1e9)

# 우선순위큐를 이용한 프림
def prim(start):
    visited = [False] * (v+1)
    distance = [INF] * (v+1)
    distance[start] = 0
    total = 0
    queue = [(0, start)]
    while queue:
        dist, now = heapq.heappop(queue)
        if visited[now]:
            continue
        visited[now] = True
        total += dist
        for n_node, w in edges[now]:
            if not visited[n_node] and w < distance[n_node]:
                distance[n_node] = w
                heapq.heappush(queue, (w, n_node))
    return total

'''
# 우선순위큐를 이용하지 않고, 일일히 최소를 찾는 프림
def prim(start):
    visited = [False] * (v+1)
    distance = [INF] * (v+1)
    distance[start] = 0
    total = 0
    for _ in range(v):
        min_dist = INF
        for idx, dist in enumerate(distance):
            if not visited[idx] and dist < min_dist:
                min_node, min_dist = idx, dist
        visited[min_node] = True
        total += min_dist
        for n_node, w in edges[min_node]:
            if not visited[n_node] and w < distance[n_node]:
                distance[n_node] = w
    return total
'''

v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]
for _ in range(e):
    x, y, w = map(int, input().split())
    edges[x].append((y, w))
    edges[y].append((x, w))
print(prim(1))
