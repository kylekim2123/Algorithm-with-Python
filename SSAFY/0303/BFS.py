def bfs(s):
    visited = [False] * (v+1)
    queue = [s] # Queue 생성
    visited[s] = True # 시작점 방문 처리
    while queue:
        node = queue.pop(0)
        print(node, end=' ') # queue에 들어간 순서대로 print (이 방식 대신, visit 배열을 만들어 한번에 출력하면 더 효율이 좋다.)
        for next_node in graph[node]:
            if not visited[next_node]: # 해당 노드에서 갈 수 있는 인접 노드 탐색
                queue.append(next_node)
                visited[next_node] = True # 방문 처리

for t in range(1, int(input())+1):
    v, e = map(int, input().split())
    graph = [[]*(v+1) for _ in range(v+1)] # 인접 리스트
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    print('#%s' % t, end=' ')
    bfs(1)
