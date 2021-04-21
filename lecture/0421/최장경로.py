def get_max_distance(start):
    global max_distance
    max_distance = max(max_distance, visited[start]) # 현재까지의 경로 수를 비교하여, 최장 경로 갱신
    for next_node in graph[start]: # 인접 노드에 대해
        if not visited[next_node]: # 방문하지 않았다면
            visited[next_node] = visited[start] + 1 # 한 칸 이동 (현재 경로 + 1)
            get_max_distance(next_node) # 그 경로를 따라서 최장 경로 탐색
            visited[next_node] = 0 # 이동 취소


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    max_distance = 0 # 최장 경로
    for i in range(1, n+1): # 모든 노드를 탐색
        visited = [0] * (n+1)
        visited[i] = 1
        get_max_distance(i)
    print('#%s %s' % (t, max_distance))