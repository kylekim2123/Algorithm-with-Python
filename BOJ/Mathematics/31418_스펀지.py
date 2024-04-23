# 실버 4

import sys

input = sys.stdin.readline
FLAG = 998_244_353


def line_length(left, limit):
    right = min(limit - left, t)
    right += left if left <= t else t + 1

    return right % FLAG


m, n, k, t = map(int, input().split())
total = 1

for _ in range(k):
    y, x = map(int, input().split())
    total *= (line_length(x, n) * line_length(y, m)) % FLAG
    total %= FLAG

print(total)
