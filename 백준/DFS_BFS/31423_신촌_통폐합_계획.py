# 골드 5

import sys

input = sys.stdin.readline


def dfs(node):
    stack = [node]

    while stack:
        node = stack.pop()
        result.append(names[node])

        while graph[node]:
            stack.append(graph[node].pop())


n = int(input())
names = [input().rstrip() for _ in range(n)]
graph = [[] for _ in range(n)]
in_degree = [0] * n
result = []

for _ in range(n - 1):
    s, e = map(lambda x: int(x) - 1, input().split())
    graph[s].append(e)
    in_degree[e] += 1

for i in range(n):
    if in_degree[i] == 0:
        dfs(i)
        break

print("".join(result))
