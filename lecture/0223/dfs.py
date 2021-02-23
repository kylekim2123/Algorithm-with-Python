def dfs_AM(v):
    stack = []
    visited = [False] * (V+1)
    stack.append(v)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            for next_node in range(1, V+1):
                if AM[node][next_node] == 1 and not visited[next_node]:
                    stack.append(next_node)


def dfs_AL(v):
    stack = []
    visited = [False] * (V+1)
    stack.append(v)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')
            for next_node in AL[node]:
                if not visited[next_node]:
                    stack.append(next_node)


V, E = 7, 8
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 6), (5, 6), (6, 7), (3, 7)]

# 인접 행렬
AM = [[0] * (V+1) for _ in range(V+1)]
for start, end in edges:
    AM[start][end], AM[end][start] = 1, 1

# 인접 리스트
AL = [[] for _ in range(V+1)]
for start, end in edges:
    AL[start].append(end)
    AL[end].append(start)

dfs_AM(1)
print()
dfs_AL(1)
