# 13458. 시험 감독 (브론즈2)

import sys

input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))
b, c = map(int, input().split())
total = len(a)

for i in a:
    i -= b
    if i > 0:
        total += i // c
        if i % c > 0:
            total += 1

print(total)
