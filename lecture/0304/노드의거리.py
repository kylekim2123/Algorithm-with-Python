def bfs(S):
    visited = [0] * (V+1) # visited는 방문체크용으로도 사용되지만, 출발점에서 해당 노드까지의 거리로도 사용됨
    queue = [S]
    visited[S] = 1
    while queue:
        node = queue.pop(0)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = visited[node] + 1 # 노드 사이의 거리는 1이므로, 다음 노드로 갈 때 1씩 더함
                if next_node == G: # 다음 노드가 도착점이라면
                    return visited[next_node] # visited 에는 출발->도착 까지의 거리가 담겨있으므로 그대로 반환
                queue.append(next_node)
    return 1 # 도착할 수 없다면 1 반환

for t in range(1, int(input())+1):
    V, E = map(int, input().split()) # 정점, 간선
    graph = [[]*(V+1) for _ in range(V+1)] # 인접 리스트
    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    S, G = map(int, input().split()) # 출발점, 도착점
    print('#%s %s' % (t, bfs(S)-1)) # 출발점에서 1로 시작했기 때문에, 결과값에서 1을 빼주어야한다.
