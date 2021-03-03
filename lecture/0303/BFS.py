def bfs(s):
    visited = [False] * (v+1)
    queue = [s]
    visited[s] = True
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = [[]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    print('#%s' % t, end=' ')
    bfs(1)
