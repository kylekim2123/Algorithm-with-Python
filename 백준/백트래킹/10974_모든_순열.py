# 실버 3

import sys

input = sys.stdin.readline


def permutations(arr):
    # 뽑고 싶은 만큼 뽑았다면 출력하고 종료
    if len(arr) == n:
        print(*arr)
        return

    # 아직 다 뽑지 못했다면 더 뽑기
    for i in range(1, n + 1):
        if not visited[i]:
            # 1) i번째 원소를 뽑는다.
            visited[i] = True
            arr.append(i)

            # 2) 재귀함수 진행
            permutations(arr)

            # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
            visited[i] = False
            arr.pop()


n = int(input())
visited = [False] * (n + 1)

permutations([])

# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
#
# n = int(input())
#
# for case in permutations(range(1, n + 1), n):
#     print(*case)
