# 실버 2

import sys
from collections import deque

input = sys.stdin.readline


def bfs(node):
    queue = deque([node])

    while queue:
        node = queue.popleft()

        for next_node in tree[node]:
            if parent[next_node] == -1:
                parent[next_node] = node
                queue.append(next_node)


n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [-1] * (n + 1)
parent[1] = 0

for _ in range(n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

bfs(1)

for i in range(2, n + 1):
    print(parent[i])
