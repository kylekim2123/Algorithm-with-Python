# 1251. 하나로

def get_dist_square(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return (x1-x2)**2 + (y1-y2)**2

def find_set(node):
    if node != p[node]:
        p[node] = find_set(p[node]) # 경로 압축
    return p[node]

for t in range(1, int(input())+1):
    n = int(input())
    nodes = list(zip(map(int, input().split()), map(int, input().split())))
    e = float(input())
    edges = sorted((get_dist_square(nodes[i], nodes[j]), i, j) for i in range(n-1)
                                                               for j in range(i+1, n))
    p = list(range(n))
    cost = 0
    for w, x, y in edges:
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root:
            p[y_root] = x_root
            cost += w
    print('#{} {:.0f}'.format(t, e * cost))


"""
Prim 알고리즘을 이용한 개선 풀이 (시간 약 10배 빠름)
edge가 너무 많아서 sort하는데 오래걸리는 경우는 크루스칼 보다 프림이 더 빠르다.


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
"""