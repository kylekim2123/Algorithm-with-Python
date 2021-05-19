# Level 3 : 가장 먼 노드

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    visited = [0] * (n+1)
    visited[1] = 1
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)
    return visited.count(max(visited))