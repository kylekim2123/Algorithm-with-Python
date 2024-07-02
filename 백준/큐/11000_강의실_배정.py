# 골드 5

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
lectures = sorted(list(map(int, input().split())) for _ in range(n))  # (시작, 종료)에 대해 오름차순 정렬
heap = [lectures[0][1]]  # 가장 빠른 강의 종료 시간을 힙에 삽입 (힙의 길이는 필요한 강의실 개수와 같음)

for start, end in lectures[1:]:
    prev_end = heappop(heap)  # 기존에 하고 있는 강의 중 가장 빨리 종료되는 시간

    if prev_end > start:  # 가장 빨리 종료되는 강의조차 현재 강의 시작 시간보다 늦게 끝나면
        heappush(heap, prev_end)  # 가장 빨리 종료되는 강의의 강의실은 사용할 수 없으므로 다시 힙에 삽입

    heappush(heap, end)  # 현재 강의가 사용하는 강의실을 힙에 삽입 (이 때 기존 강의실을 재사용하거나, 새로 추가)

print(len(heap))
