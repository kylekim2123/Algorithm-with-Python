# 2930. 힙

from heapq import heappush, heappop

for t in range(1, int(input())+1):
    n = int(input())
    heap = []
    result = [f'#{t}']
    for _ in range(n):
        control = list(map(int, input().split()))
        if control[0] == 1:
            heappush(heap, (-control[1], control[1]))
            continue
        if len(heap) == 0:
            result.append(-1)
            continue
        result.append(heappop(heap)[1])
    print(*result)