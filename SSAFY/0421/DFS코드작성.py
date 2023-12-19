def dfs(node):
    result.append(node)
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    result = []
    dfs(1)
    print('#%s %s' % (t, ' '.join(map(str, result))))