# 1197. 최소 스패닝 트리 (골드4)

import sys
input = sys.stdin.readline
INF = int(1e9)

# Prim
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