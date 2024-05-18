# 실버 4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
start, end, total, result = 0, 0, numbers[0], 0

while end < n:
    if total < m:
        if end == n - 1:
            break

        end += 1
        total += numbers[end]
    else:
        if total == m:
            result += 1

        total -= numbers[start]
        start += 1

        if end < start < n:
            end = start
            total = numbers[start]

print(result)
