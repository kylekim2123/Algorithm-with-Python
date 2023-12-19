INF = int(1e13)

def prim(start):
    visited = [False] * n
    D = [INF] * n # key
    D[start] = 0
    total = 0
    for _ in range(n):
        # 인접한 노드로 가는 간선 중 최소 비용의 간선을 고르는 과정
        min_d = INF
        for i, d in enumerate(D):
            if not visited[i] and d < min_d: # 사이클 방지
                min_node, min_d = i, d
        visited[min_node] = True # 방문처리
        total += min_d # 간선이 선택될 때마다 total에 더함

        # 최소 비용의 간선으로 도달하는 노드에 대해, 그 인접 노드로 가는 간선 정보 모두 저장
        for n_node, n_d in graph[min_node]:
            if not visited[n_node] and n_d < D[n_node]: # 사이클 방지
                D[n_node] = n_d
    return total
    

for t in range(1, int(input())+1):
    n = int(input())
    X, Y = list(map(int, input().split())), list(map(int, input().split()))
    e = float(input())
    graph = [[] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            w = (X[i]-X[j])**2 + (Y[i]-Y[j])**2 # 피타고라스 정리 (두 좌표 사이의 거리의 제곱)
            graph[i].append((j, w))
            graph[j].append((i, w))
    print('#{} {:.0f}'.format(t, e * prim(0)))