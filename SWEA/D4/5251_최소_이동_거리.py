# D4

### 1) 단순 반복문을 이용한 다익스트라
INF = 9999999


def dijkstra(start):
    visited = [False] * (n + 1)  # 최단 경로 확정을 위한 방문 처리 배열
    distance[start] = 0  # 출발 정점은 거리 0으로 초기화

    for _ in range(n):  # 0 ~ n-1 정점만 탐색해도 n번째 정점까지의 최단 경로가 도출됨
        # 1. 최단 거리가 확정되지 않은 정점들 중 가장 짧은 경로의 정점 선택
        node, min_dist = -1, INF

        for i in range(n + 1):
            if not visited[i] and min_dist > distance[i]:
                node = i
                min_dist = distance[i]

        # 2. 해당 정점에 대한 최단 거리 확정
        visited[node] = True

        # 3. 해당 정점과 인접한 정점들에 대한 최단 경로 갱신
        for next_node, dist in graph[node]:
            next_dist = distance[node] + dist

            if not visited[next_node] and next_dist < distance[next_node]:
                distance[next_node] = next_dist


### 2) 힙을 이용한 다익스트라
# from heapq import heappush, heappop
#
# INF = 9999999
#
#
# def dijkstra(start):
#     distance[start] = 0  # 출발 정점 방문
#     heap = [(0, start)]
#
#     while heap:
#         min_dist, node = heappop(heap)  # 갈 수 있는 정점 중 가장 최단 경로의 정점을 선택
#
#         if distance[node] < min_dist:
#             continue  # 그런데 이미 최단 경로로 기록된 값보다 큰 경우, 탐색할 필요가 없음
#
#         for next_node, dist in graph[node]:  # 해당 정점과 인접한 다음 정점들에 대해
#             next_dist = min_dist + dist  # 다음 정점까지의 거리를 계산하고
#
#             if next_dist < distance[next_node]:  # 다음 정점에 기록된 최단 경로보다 더 짧은 경우
#                 distance[next_node] = next_dist  # 다음 정점의 최단 경로를 갱신
#                 heappush(heap, (next_dist, next_node))  # 탐색을 해야 하므로 힙에 삽입

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for _ in range(m):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    dijkstra(0)  # 0번 정점에서 출발

    print(f"#{test_case} {distance[n]}")
