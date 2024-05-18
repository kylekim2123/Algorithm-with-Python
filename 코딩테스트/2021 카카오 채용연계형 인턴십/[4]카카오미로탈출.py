# 4. 라이언의 카카오 미로 탈출

from heapq import heappop, heappush
from copy import deepcopy
INF = int(1e9)

def reverse_roads(now_node, now_graph):
    temp = deepcopy(now_graph)
    for i in range(len(temp[now_node])):
        temp[now_node][i][2] = not temp[now_node][i][2]

        next_node = temp[now_node][i][0]
        for j in range(len(temp[next_node])):
            if temp[next_node][j][0] == now_node:
                temp[next_node][j][2] = not temp[next_node][j][2]
    return temp

def dijkstra(n, start, end, graph, traps):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = [(0, start, graph)]
    while queue:
        now_w, now_node, now_graph = heappop(queue)
        if now_node == end:
            return now_w
        for next_node, next_w, is_connected in now_graph[now_node]:
            if not is_connected:
                continue
            changed_w = now_w + next_w
            distance[next_node] = changed_w
            if next_node in traps:
                heappush(queue, (changed_w, next_node, reverse_roads(next_node, now_graph)))
            else:
                heappush(queue, (changed_w, next_node, now_graph))
    return distance[end]

def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n+1)]
    for s, e, w in roads:
        for i in range(len(graph[s])):
            if e == graph[s][i][0] and w < graph[s][i][1]:
                graph[s][i][1] = w
                graph[e][i][1] = w
                break
        else:
            graph[s].append([e, w, True])
            graph[e].append([s, w, False])
    return dijkstra(n, start, end, graph, set(traps))
    
n, start, end = 4, 1, 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))