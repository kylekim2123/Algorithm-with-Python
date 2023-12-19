# dfs를 재귀로 구현
def dfs(node):
    visited[node] = 1
    for next_node in AL[node]:
        if not visited[next_node]:
            dfs(next_node)

SIZE, A, B = 100, 0, 99
for _ in range(1, 11):
    t, n = map(int, input().split()) # 테스트 케이스, 정점
    edges = list(map(int, input().split())) # 간선
    AL = [[] for _ in range(SIZE)]
    for i in range(0, n*2-1, 2):
        AL[edges[i]].append(edges[i+1]) # AL에 간선 정보 등록(단방향)

    visited = [0] * SIZE
    dfs(A)
    print('#%s %s' % (t, visited[B]))
