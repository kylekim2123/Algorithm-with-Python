# 골드 2

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, k = map(int, input().split())
jewelries = sorted([list(map(int, input().split())) for _ in range(n)])
bags = sorted([int(input()) for _ in range(k)])
queue = []
total = 0
i = 0

for bag in bags:
    while i < n and bag >= jewelries[i][0]:
        heappush(queue, -jewelries[i][1])
        i += 1

    if queue:
        total += heappop(queue)

print(-total)
