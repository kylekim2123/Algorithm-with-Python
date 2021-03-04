def bfs(S):
    visited = [0] * (V+1)
    queue = [S]
    visited[S] = 1
    while queue:
        node = queue.pop(0)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = visited[node] + 1
                if next_node == G:
                    return visited[next_node]
                queue.append(next_node)
    return 1

for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    S, G = map(int, input().split())
    print('#%s %s' % (t, bfs(S)-1))
