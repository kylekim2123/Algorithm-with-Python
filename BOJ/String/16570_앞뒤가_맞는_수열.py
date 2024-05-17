# 플래티넘 5

import sys

input = sys.stdin.readline


def make_table(numbers):
    table = [0]
    i = 0

    for j in range(1, len(numbers)):
        while i > 0 and numbers[i] != numbers[j]:
            i = table[i - 1]

        if numbers[i] == numbers[j]:
            i += 1

        table.append(i)

    return table


n = int(input())
numbers = list(map(int, input().split()))
table = make_table(numbers[::-1])
max_result = max(table)

if max_result == 0:
    print(-1)
else:
    print(max_result, table.count(max_result))
