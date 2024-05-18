# 플래티넘 5

import sys
from collections import deque

input = sys.stdin.readline


def topology_sort(graph, in_degree, max_dist):
    queue = deque([node for node in range(1, n + 1) if in_degree[node] == 0])

    while queue:
        node = queue.popleft()

        for next_node, dist in graph[node]:
            in_degree[next_node] -= 1
            max_dist[next_node] = max(max_dist[next_node], max_dist[node] + dist)

            if in_degree[next_node] == 0:
                queue.append(next_node)


def bfs(node):
    visited = [False] * (n + 1)
    visited[node] = True
    queue = deque([node])
    max_edges = 0

    while queue:
        node = queue.popleft()

        for next_node, dist in forward_graph[node]:
            path_weight = forward_max_dist[node] + dist + reverse_max_dist[next_node]
            if path_weight == forward_max_dist[end]:
                max_edges += 1

            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return max_edges


n, m = int(input()), int(input())
forward_graph = [[] for _ in range(n + 1)]
forward_in_degree = [0] * (n + 1)
forward_max_dist = [0] * (n + 1)
reverse_graph = [[] for _ in range(n + 1)]
reverse_in_degree = [0] * (n + 1)
reverse_max_dist = [0] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    forward_graph[s].append((e, w))
    forward_in_degree[e] += 1
    reverse_graph[e].append((s, w))
    reverse_in_degree[s] += 1

start, end = map(int, input().split())

topology_sort(forward_graph, forward_in_degree, forward_max_dist)
topology_sort(reverse_graph, reverse_in_degree, reverse_max_dist)

print(forward_max_dist[end])  # 도착 도시에서 만나는 시간 (최대 거리)
print(bfs(start))  # 쉬지 않고 달려야 하는 도로의 개수 (최대 거리를 이루는 간선의 수)
