# 실버 3

import sys

input = sys.stdin.readline


def combinations_with_replacement(depth, start, total):
    if depth == n:
        totals.add(total)
        return

    for i in range(start, len(numbers)):
        combinations_with_replacement(depth + 1, i, total + numbers[i])


n = int(input())
numbers = [1, 5, 10, 50]
totals = set()

combinations_with_replacement(0, 0, 0)

print(len(totals))

# import sys
# from itertools import combinations_with_replacement
#
# input = sys.stdin.readline
#
# n = int(input())
# numbers = [1, 5, 10, 50]
#
# totals = {sum(case) for case in combinations_with_replacement(numbers, n)}
#
# print(len(totals))
