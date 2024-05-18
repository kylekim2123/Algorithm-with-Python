# 1967. 트리의 지름 (골드4)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(node, length):
    global end_point, diameter
    if length > diameter:
        end_point = node
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
end_point, diameter = 0, 0
dfs(1, 0)
dfs(end_point, 0)
print(diameter)