# 플래티넘 5

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


while True:
    s = input().rstrip()

    if s == ".":
        break

    if s[0] * len(s) == s:
        print(len(s))
        continue

    table = make_table(s)
    pattern_length = len(s) - table[-1]

    if pattern_length == 0:
        print(0)
    else:
        print(len(s) // pattern_length if len(s) % pattern_length == 0 else 1)
