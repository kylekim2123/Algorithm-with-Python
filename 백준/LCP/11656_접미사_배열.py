# 실버 4

import sys

input = sys.stdin.readline
TOP, FIRST = 0, 1


def counting_sort(original, index, max_number):
    counter = [0] * (max_number + 1)
    result = [None] * len(original)

    for i in range(len(original)):
        counter[original[i][index]] += 1

    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]

    for i in range(len(original) - 1, -1, -1):
        counter[original[i][index]] -= 1
        result[counter[original[i][index]]] = original[i]

    return result


def next_rank(suffixes):
    rank = [FIRST] * len(suffixes)

    for i in range(1, len(suffixes)):
        rank[suffixes[i][2]] = rank[suffixes[i - 1][2]]

        if suffixes[i - 1][0] != suffixes[i][0] or suffixes[i - 1][1] != suffixes[i][1]:
            rank[suffixes[i][2]] += 1

    return rank


def make_suffixes(word):
    n, t = len(word), 1
    rank = [ord(char) - 96 for char in word]  # 순위는 1부터 시작하도록 97이 아닌 96을 뺌

    while t < n:
        max_rank = max(rank)

        if t > 1 and max_rank == n:
            break

        suffixes = [(rank[i], rank[i + t] if i + t < n else TOP, i) for i in range(n)]  # (기존 순위, 현재 순위, 인덱스)
        suffixes = counting_sort(suffixes, 1, max_rank)
        suffixes = counting_sort(suffixes, 0, max_rank)

        rank = next_rank(suffixes)
        t *= 2

    return [suffix[2] for suffix in suffixes]


word = input().rstrip()
print(*[word[i:] for i in make_suffixes(word)], sep="\n")
