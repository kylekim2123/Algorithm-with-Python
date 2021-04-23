INF = int(1e13)

def prim(start):
    visited = [False] * n
    D = [INF] * n
    D[start] = 0
    total = 0
    for _ in range(n):
        min_d = INF
        for i, d in enumerate(D):
            if not visited[i] and d < min_d:
                min_node, min_d = i, d
        visited[min_node] = True
        total += min_d
        for n_node, n_d in graph[min_node]:
            if not visited[n_node] and n_d < D[n_node]:
                D[n_node] = n_d
    return total
    

for t in range(1, int(input())+1):
    n = int(input())
    X, Y = list(map(int, input().split())), list(map(int, input().split()))
    e = float(input())
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            w = (X[i]-X[j])**2 + (Y[i]-Y[j])**2
            graph[i].append((j, w))
            graph[j].append((i, w))
    print('#{} {:.0f}'.format(t, e * prim(0)))