def get_max_distance(start):
    global max_distance
    max_distance = max(max_distance, visited[start])
    for next_node in graph[start]:
        if not visited[next_node]:
            visited[next_node] = visited[start] + 1
            get_max_distance(next_node)
            visited[next_node] = 0


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    max_distance = 0
    for i in range(1, n+1):
        visited = [0] * (n+1)
        visited[i] = 1
        get_max_distance(i)
    print('#%s %s' % (t, max_distance))