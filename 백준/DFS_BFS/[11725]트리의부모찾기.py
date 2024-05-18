# 11725. 트리의 부모 찾기 (실버2)

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs1(node):
    for next_node in tree[node]:
        if not visited[next_node]:
            visited[next_node] = node
            dfs1(next_node)

def dfs2(start):
    stack = [start]
    while stack:
        node = stack.pop()
        for next_node in tree[node]:
            if not visited[next_node]:
                stack.append(next_node)
                visited[next_node] = node

n = int(input())
tree = [[]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

visited = [0] * (n+1)
visited[1] = 1
dfs2(1)
print(*visited[2:], sep='\n')