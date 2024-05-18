# 골드 3

import sys
from collections import deque

input = sys.stdin.readline


def topology_sort():
    queue = deque()

    for node in range(1, m + 1):
        if in_degree[node] == 0:
            queue.append(node)
            order[node] = [1]

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if not order[next_node] or order[next_node][0] < order[node][0]:
                order[next_node] = [order[node][0], 1]
            else:
                order[next_node][1] += 1

            in_degree[next_node] -= 1

            if in_degree[next_node] == 0:
                queue.append(next_node)

                if order[next_node][1] >= 2:
                    order[next_node] = [order[next_node][0] + 1]
                else:
                    order[next_node] = [order[next_node][0]]


for _ in range(int(input())):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    in_degree = [0] * (m + 1)

    for _ in range(p):
        s, e = map(int, input().split())
        graph[s].append(e)
        in_degree[e] += 1

    order = [[] for _ in range(m + 1)]
    topology_sort()

    print(k, order[m][0])
