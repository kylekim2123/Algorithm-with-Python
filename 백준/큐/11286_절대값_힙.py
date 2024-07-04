# 실버 1

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heappush(heap, (abs(x), x))  # x가 0이 아니라면 (절대값, 원본)을 힙에 삽입
        continue

    if heap:
        print(heappop(heap)[1])  # x가 0이고 힙이 비어있지 않으면 원본을 출력
    else:
        print(0)  # x가 0이고 힙이 비어있으면 0을 출력
