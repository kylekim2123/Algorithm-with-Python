# 1967. 트리의 지름 (골드4)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(node, length):
    global diameter
    if length > diameter:
        diameter = length
    visited[node] = 1
    for next_node, weight in tree[node]:
        if not visited[next_node]:
            dfs(next_node, length + weight)
    visited[node] = 0

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, w = map(int, input().split())
    tree[s].append((e, w))
    tree[e].append((s, w))

visited = [0] * (n+1)
diameter = 0
for i in range(1, n+1):
    if not visited[i] and len(tree[i]) == 1:
        dfs(i, 0)
        visited[i] = 1
print(diameter)