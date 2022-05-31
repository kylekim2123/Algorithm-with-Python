# 1874. 스택 수열 (실버 3)

import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
stack, result = [], []

i, j = 0, 1

while i < n:
    if not stack or stack[-1] < numbers[i]:
        stack.append(j)
        result.append("+")
        j += 1
        continue

    if stack[-1] == numbers[i]:
        stack.pop()
        result.append("-")
        i += 1
        continue

    print("NO")
    break
else:
    print(*result, sep="\n")
