# 골드 1

import sys

input = sys.stdin.readline

n = int(input())
s = input().rstrip()
changes = [i + 1 for i in range(n - 1) if s[i] != s[i + 1]]

if s[-1] == "B" and len(changes) <= 1:
    print(-1)
else:
    if s[-1] == "B":
        changes[-2], changes[-1] = changes[-1], changes[-2]

    print(len(changes), "\n".join(map(str, changes)), sep="\n")
