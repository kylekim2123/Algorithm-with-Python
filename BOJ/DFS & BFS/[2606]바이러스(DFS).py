# 2606. 바이러스(DFS) (실버3)

def dfs(start):
    visited[start] = True
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(next_node)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n+1)
dfs(1)
print(visited.count(True)-1)