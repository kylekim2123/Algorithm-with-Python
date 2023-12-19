# 풀이4. 인접행렬 사용
def dfs(v):
    visited[v] = True
    for next_node in range(1, V+1):
        if graph[v][next_node] == 1 and not visited[next_node]:
            dfs(next_node)


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for start, end in edges:
        graph[start][end] = 1

    stack = []
    visited = [False] * (V+1)
    dfs(S)
    if visited[G]:
        print('#%s 1' % t)
    else:
        print('#%s 0' % t)
