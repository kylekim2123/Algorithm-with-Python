# dfs를 스택과 반복문으로 구현
def dfs(start):
    stack = []
    visited = [0] * SIZE
    stack.append(start) # 시작점 삽입
    while stack:
        node = stack.pop() # 최상단 노드 꺼냄
        if not visited[node]:
            if node == B: # 방문한 곳이 B라면 1을 리턴
                return 1
            visited[node] = 1 # 방문처리
            for next_node in AL[node]:
                if not visited[next_node]:
                    stack.append(next_node) # 해당 노드와 연결된 다음 노드들 스택에 삽입
    return 0


SIZE, A, B = 100, 0, 99
for _ in range(1, 11):
    t, n = map(int, input().split()) # 테스트 케이스, 정점
    edges = list(map(int, input().split())) # 간선
    AL = [[] for _ in range(SIZE)]
    for i in range(0, n*2-1, 2):
        AL[edges[i]].append(edges[i+1]) # AL에 간선 정보 등록(단방향)

    print('#%s %s' % (t, dfs(A)))