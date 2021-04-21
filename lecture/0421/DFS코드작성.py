def dfs(node):
    result.append(node)
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    for i in range(0, e+e, 2):
        graph[edges[i]].append(edges[i+1])
        graph[edges[i+1]].append(edges[i])

    result = []
    dfs(1)
    print('#%s %s' % (t, '-'.join(map(str, result))))