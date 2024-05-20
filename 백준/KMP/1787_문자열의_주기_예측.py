# 플래티넘 2

import sys

input = sys.stdin.readline


def make_table(word):
    table = [0]
    i = 0

    for j in range(1, len(word)):
        while i > 0 and word[i] != word[j]:
            i = table[i - 1]

        if word[i] == word[j]:
            i += 1

        table.append(i)

    return table


n = int(input())
s = input().rstrip()
dp = [0] * n
total = 0

for i, t in enumerate(make_table(s)):
    if t > 0:
        dp[i] = t if dp[t - 1] == 0 else dp[t - 1]
        total += (i + 1) - dp[i]

print(total)
