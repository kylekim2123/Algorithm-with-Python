# 실버 2

# import sys
#
# input = sys.stdin.readline
#
#
# def combinations(arr, start, total):
#     if arr and total == s:
#         global result
#         result += 1
#
#     for i in range(start, len(numbers)):
#         # 1) i번째 원소를 뽑는다.
#         arr.append(numbers[i])
#
#         # 2) 재귀함수 진행
#         combinations(arr, i + 1, total + numbers[i])
#
#         # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
#         arr.pop()
#
#
# n, s = map(int, input().split())
# numbers = list(map(int, input().split()))
# result = 0
#
# combinations([], 0, 0)
#
# print(result)

import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

for i in range(1, n + 1):
    for case in combinations(numbers, i):
        if sum(case) == s:
            result += 1

print(result)
