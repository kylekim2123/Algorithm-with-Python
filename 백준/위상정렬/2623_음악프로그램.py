# 골드 3

import sys
from collections import deque

input = sys.stdin.readline


def topology_sort():
    queue = deque([node for node in range(1, n + 1) if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for next_node in graph[node]:
            in_degree[next_node] -= 1

            if in_degree[next_node] == 0:
                queue.append(next_node)

    return result


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
    length, *singers = map(int, input().split())

    for i in range(length - 1):
        graph[singers[i]].append(singers[i + 1])
        in_degree[singers[i + 1]] += 1

result = topology_sort()

if len(result) == n:
    print(*result, sep="\n")
else:
    print(0)
