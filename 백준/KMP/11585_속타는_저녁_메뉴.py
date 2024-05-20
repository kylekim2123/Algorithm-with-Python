# 플래티넘 5

import math
import sys

input = sys.stdin.readline


def make_table(pattern):
    table = [0]
    i = 0

    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]

        if pattern[i] == pattern[j]:
            i += 1

        table.append(i)

    return table


def kmp(parent, pattern):
    table = make_table(pattern)
    count, j = 0, 0

    for i in range(len(parent) - 1):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                count += 1
                j = table[j]
            else:
                j += 1

    return count


n = int(input())
pattern = input().split()
parent = input().split() * 2

meat_counts = kmp(parent, pattern)
gcd = math.gcd(meat_counts, n)

print(f"{meat_counts // gcd}/{n // gcd}")
