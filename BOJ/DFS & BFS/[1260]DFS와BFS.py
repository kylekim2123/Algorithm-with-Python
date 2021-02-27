# 1260. DFS와 BFS (실버2)

import sys
from collections import deque

def dfs(start):
    visited.add(start)
    print(start, end=' ')
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(next_node)

def bfs(start):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for edge in graph:
    edge.sort()

visited = set()
dfs(v)
print()
visited = set()
bfs(v)
