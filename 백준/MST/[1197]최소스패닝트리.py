# 1197. 최소 스패닝 트리 (골드4)

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

# Prim
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

v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]
for _ in range(e):
    x, y, w = map(int, input().split())
    edges[x].append((y, w))
    edges[y].append((x, w))
print(prim(1))


'''
# Kruskal
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

v, e = map(int, input().split())
edges = []
for _ in range(e):
    x, y, w = map(int, input().split())
    edges.append((w, x, y))
edges.sort()

parent = list(range(v+1))
total, count = 0, 0
for w, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root
        total += w
        count += 1
        if count >= v-1:
            break
print(total)
'''