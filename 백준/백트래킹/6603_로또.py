# 실버 2

import sys
from itertools import combinations

input = sys.stdin.readline


# def combinations(arr, start):
#     # 뽑고 싶은 만큼 뽑았다면 출력하고 종료
#     if len(arr) == 6:
#         print(*arr)
#         return
#
#     # 아직 다 뽑지 못했다면 더 뽑기
#     for i in range(start, len(s)):
#         # 1) i번째 원소를 뽑는다.
#         arr.append(s[i])
#
#         # 2) 재귀함수 진행
#         combinations(arr, i + 1)
#
#         # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
#         arr.pop()


while True:
    k, *s = map(int, input().split())

    if k == 0:
        break

    for case in combinations(s, 6):
        print(*case)

    # combinations([], 0)
    print()
