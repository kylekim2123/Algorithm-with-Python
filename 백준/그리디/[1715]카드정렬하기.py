# 1715. 카드 정렬하기 (골드4)

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
cards = sorted(int(input()) for _ in range(n))
total = 0
while len(cards) > 1:
    plused = heappop(cards) + heappop(cards)
    total += plused
    heappush(cards, plused)
print(total)
