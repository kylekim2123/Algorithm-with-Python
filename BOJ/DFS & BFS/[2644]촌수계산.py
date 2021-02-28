# 2644. 촌수계산 (실버2)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(node):
    for next_node in family[node]:
        if not visited[next_node]:
            visited[next_node] = visited[node] + 1
            dfs(next_node)

n = int(input())
r1, r2 = map(int, input().split())
m = int(input())
family = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    family[s].append(e)
    family[e].append(s)

visited = [0] * (n+1)
visited[r1] = 1
dfs(r1)
print(visited[r2]-1) if visited[r2] else print(-1)
