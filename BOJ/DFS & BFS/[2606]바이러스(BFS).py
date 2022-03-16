# 2606. 바이러스 (실버3) - BFS

from collections import deque


def bfs(node):
    queue = deque([node])
    visited[node] = True
    total = -1
    while queue:
        node = queue.popleft()
        total += 1
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    return total


n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

print(bfs(1))
