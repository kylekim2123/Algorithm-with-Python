# 실버 3

# import sys
#
# input = sys.stdin.readline
#
#
# def product(arr):
#     # 뽑고 싶은 만큼 뽑았다면 출력하고 종료
#     if len(arr) == m:
#         print(*arr)
#         return
#
#     # 아직 다 뽑지 못했다면 더 뽑기
#     for i in range(len(numbers)):
#         # 1) i번째 원소를 뽑는다.
#         arr.append(numbers[i])
#
#         # 2) 재귀함수 진행
#         product(arr)
#
#         # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
#         arr.pop()
#
#
# n, m = map(int, input().split())
# numbers = sorted(map(int, input().split()))
#
# product([])

import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

for case in product(numbers, repeat=m):
    print(*case)
