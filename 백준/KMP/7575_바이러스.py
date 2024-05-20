# 플래티넘 5

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


def kmp(parent, pattern, table):
    j = 0

    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True

            j += 1

    return False


def check_virus(codes):
    min_length, min_code = codes[0]
    codes = codes[1:]

    for start in range(min_length - k + 1):
        virus = min_code[start:start + k]
        table = make_table(virus)

        reversed_virus = virus[::-1]
        reversed_table = make_table(reversed_virus)

        for _, code in codes:
            if not kmp(code, virus, table) and not kmp(code, reversed_virus, reversed_table):
                break
        else:
            return "YES"

    return "NO"


n, k = map(int, input().split())
codes = sorted(([int(input()), list(map(int, input().split()))] for _ in range(n)), key=lambda x: x[0])

print(check_virus(codes))
