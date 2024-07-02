# 골드 4

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
heap = []
total = 0

for _ in range(n):
    heappush(heap, int(input()))  # 힙 구조에 맞게 삽입

while len(heap) > 1:  # 카드 뭉치가 하나로 모일 때 까지 반복
    compare_counts = heappop(heap) + heappop(heap)  # 가장 적은 카드 뭉치 두 개를 꺼내 합침
    total += compare_counts  # 결과 누적
    heappush(heap, compare_counts)  # 합친 카드 뭉치는 또다른 카드 뭉치와 합쳐야 하므로 힙에 삽입

print(total)
