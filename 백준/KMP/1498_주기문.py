# 플래티넘 4

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


word = input().rstrip()
table = make_table(word)

for i, t in enumerate(table):
    length = i + 1
    pattern_length = length - t

    if pattern_length > 0 and length % pattern_length == 0 and length // pattern_length >= 2:
        print(length, length // pattern_length)
