# 1697. 숨바꼭질 (실버1)

import sys
from collections import deque
input = sys.stdin.readline
DX = [-1, 1, 2]

def bfs(start):
    visited = [0] * 100001
    visited[start] = 1
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for d in DX:
            nx = x+x if d == 2 else x+d
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                if nx == k:
                    return visited[nx]-1
                queue.append(nx)

n, k = map(int, input().split())
result = n-k if n >= k else bfs(n)
print(result)