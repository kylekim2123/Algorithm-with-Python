# 실버 1

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heap = []

for card in cards:
    heappush(heap, card)  # 카드를 모두 힙에 삽입하여 최소힙의 형태를 만듦

for _ in range(m):
    card_x = heappop(heap)  # x번 카드 꺼내기
    card_y = heappop(heap)  # y번 카드 꺼내기

    total = card_x + card_y  # x번 카드와 y번 카드 더하기

    heappush(heap, total)  # x번 카드 덮어쓰기
    heappush(heap, total)  # y번 카드 덮어쓰기

print(sum(heap))  # 합체가 모두 끝난 뒤의 카드의이 총합
