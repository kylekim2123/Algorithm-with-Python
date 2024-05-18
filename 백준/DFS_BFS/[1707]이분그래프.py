# 1707. 이분 그래프 (골드4)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    queue = deque([s])
    visited[s] = 1
    while queue:
        node = queue.popleft()
        color = 3 - visited[node]
        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = color
            elif visited[node] == visited[next_node]:
                return 'NO'
    return 'YES'

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int, input().split())
        if start == end:
            continue
        graph[start].append(end)
        graph[end].append(start)

    visited = [0] * (v+1)
    for i in range(1, v+1):
        if not visited[i]: # 시간초과 방지의 핵심(모든 정점을 다 볼 필요는 없다. 방문하지 않은 곳만 보면 된다.)
            if bfs(i) == 'NO': # 어느 정점에서 No라고 판별되면 다른 정점을 볼 필요가 없다.
                print('NO')
                break
    else:
        print('YES')
