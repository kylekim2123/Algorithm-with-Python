# 실버 2

import sys

input = sys.stdin.readline


# 힙 삽입 연산
def heap_push(item):
    heap.append(item)

    child = len(heap) - 1
    parent = child // 2

    while parent > 0 and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


# 힙 삭제 연산
def heap_pop():
    if len(heap) <= 2:
        return heap.pop()

    root = heap[1]
    heap[1] = heap.pop()

    parent = 1
    child = parent * 2

    while child < len(heap):
        if child + 1 < len(heap) and heap[child] < heap[child + 1]:
            child += 1

        if heap[parent] >= heap[child]:
            break

        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2

    return root


n = int(input())
heap = [-1]

for _ in range(n):
    x = int(input())

    if x == 0:
        print(heap_pop() if len(heap) > 1 else 0)
    else:
        heap_push(x)

### heapq 모듈 사용 ###
# import sys
# from heapq import heappop, heappush
#
# input = sys.stdin.readline
#
# heap = []
#
# for _ in range(int(input())):
#     x = int(input())
#
#     if x == 0:
#         print(-heappop(heap) if heap else 0)
#     else:
#         heappush(heap, -x)
