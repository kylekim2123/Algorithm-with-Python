# 1260. DFS와 BFS (실버2)

import sys
from collections import deque
input = sys.stdin.readline


def dfs(node):
    visited[node] = True
    print(node, end=" ")
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)


def bfs(node):
    queue = deque([node])
    visited[node] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for edge in graph:
    edge.sort()

visited = [False] * (n + 1)
dfs(v)

print()

visited = [False] * (n + 1)
bfs(v)
