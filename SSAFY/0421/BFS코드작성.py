def bfs(start):
    queue = [start]
    visited = [False] * (v+1)
    visited[start] = True
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)


for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    print('#%s' % t, end=' ')
    bfs(1)