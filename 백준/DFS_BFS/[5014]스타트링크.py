# 5014. 스타트링크 (골드5)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    building = [0] * (F+1)
    queue = deque([start])
    building[start] = 1
    while queue:
        floor = queue.popleft()
        for button in [U, -D]:
            next_floor = floor + button
            if 0 < next_floor <= F and not building[next_floor]:
                building[next_floor] = building[floor] + 1
                if next_floor == G:
                    return building[next_floor] - 1
                queue.append(next_floor)
    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
if S == G:
    result = 0
elif (S > G and not D) or (S < G and not U):
    result = 'use the stairs'
else:
    result = bfs(S)
print(result)