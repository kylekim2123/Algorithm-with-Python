# 1389. 케빈 베이컨의 6단계 법칙 (실버1)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [0] * (n+1)
    queue = deque([start])
    visited[start] = 1
    while queue:
        person = queue.popleft()
        for next_person in friends[person]:
            if not visited[next_person]:
                visited[next_person] = visited[person] + 1
                queue.append(next_person)
    return sum(visited) - n

n, m = map(int, input().split())
friends = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    friends[s].append(e)
    friends[e].append(s)

min_step = 987654321
for i in range(1, n+1):
    step = bfs(i)
    if min_step > step:
        min_step = step
        min_index = i
print(min_index)
