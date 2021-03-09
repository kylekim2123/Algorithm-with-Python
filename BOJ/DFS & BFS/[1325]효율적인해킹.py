# 1325. 효율적인 해킹(실버2)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [0] * (n+1)
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[start] += 1
                visited[next_node] = 1
                queue.append(next_node)
    return visited[start]

n, m = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[e].append(s)

max_result, result = 0, []
for i in range(1, n+1):
    temp = bfs(i)
    if temp >= max_result:
        result.append((i, temp))
        max_result = temp

print(*[res[0] for res in result if max_result == res[1]])
