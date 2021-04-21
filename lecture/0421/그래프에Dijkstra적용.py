INF = 987654321

# D배열에서 최단 경로의 노드 찾기
def shortest_node():
    index, min_value = 0, INF
    for i, value in enumerate(D):
        if not U[i] and value < min_value:
            index, min_value = i, value
    return index


# 다익스트라
def find_shortest(start):
    # 시작 포인트 초기화
    U[start] = True
    D[start] = 0
    for next_node, weight in graph[start]:
        D[next_node] = weight
    
    # 시작노드를 제외한 나머지 노드까지의 최단 경로 탐색
    for _ in range(n-2): # n-2인 이유는, 마지막 노드도 탐색하지 않아도 되기 때문
        now = shortest_node() # 인접 노드 중 최단 거리에 있는 노드
        U[now] = True # 방문 처리
        for next_node, weight in graph[now]: # 해당 노드에서 갈 수 있는 인접 노드를 대상
            if not U[next_node]: # 인접 노드 아직 방문 안했다면
                D[next_node] = min(D[next_node], D[now] + weight) # 인접 노드의 현재 최단거리 vs 새로 갔을 때 거리


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        s, e, w = input().split()
        graph[ord(s)-97].append((ord(e)-97, int(w)))

    U = [False] * n # 방문처리 배열
    D = [INF] * n # 최단경로 배열
    find_shortest(0)
    print('#%s %s' % (t, ' '.join(map(str, D))))