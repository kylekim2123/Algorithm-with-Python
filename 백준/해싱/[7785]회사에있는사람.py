# 7785. 회사에 있는 사람 (실버5)

import sys

input = sys.stdin.readline

logs = {}
for _ in range(int(input())):
    name, status = input().split()
    logs[name] = status

print(*sorted((name for name in logs if logs[name] == "enter"), reverse=True), sep="\n")
