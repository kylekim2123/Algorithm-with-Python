def bfs(v):
    visited = [False] * (V+1)
    queue = [v] # 시작 노드 큐에 추가
    visited[v] = True # 시작 노드 방문 처리
    while queue:
        node = queue.pop(0) # 큐의 앞쪽 원소 pop
        for next_node in graph[node]:
            if not visited[next_node]: # 방문하지 않은 인접 노드에 대해
                queue.append(next_node) # 큐에 삽입
                visited[next_node] = True # 방문 처리


V, E = map(int, input().split()) # 정점, 간선 개수
edges = [list(map(int, input().split())) for _ in range(E)] # 간선 정보(시작, 끝)
S, G = map(int, input().split()) # 출발, 도착

graph = [[] for _ in range(V+1)]
for start, end in edges:
    graph[start].append(end) # 단방향
    graph[end].append(start) # 양방향
