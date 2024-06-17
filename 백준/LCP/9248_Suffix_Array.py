# 플래티넘 3

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


def get_next_rank(suffixes):
    rank = [FIRST] * len(suffixes)

    for i in range(1, len(suffixes)):
        rank[suffixes[i][2]] = rank[suffixes[i - 1][2]]

        if suffixes[i - 1][0] != suffixes[i][0] or suffixes[i - 1][1] != suffixes[i][1]:
            rank[suffixes[i][2]] += 1

    return rank


def get_suffix_array_and_rank(word):
    n, t = len(word), 1
    rank = [ord(char) - 96 for char in word]

    while t < n:
        max_rank = max(rank)

        if t > 1 and max_rank == n:
            break

        suffixes = [(rank[i], rank[i + t] if i + t < n else TOP, i) for i in range(n)]
        suffixes = counting_sort(suffixes, 1, max_rank)
        suffixes = counting_sort(suffixes, 0, max_rank)

        rank = get_next_rank(suffixes)
        t *= 2

    return [suffix[2] for suffix in suffixes], rank


def get_lcp(word, suffix_array, rank):
    n, k = len(word), 0
    lcp = ["x"] * len(word)

    for i in range(n):
        k = max(k - 1, 0)

        if rank[i] == 1:
            continue

        j = suffix_array[rank[i] - 2]

        while i + k < n and j + k < n and word[i + k] == word[j + k]:
            k += 1

        lcp[rank[i] - 1] = k

    return lcp


word = input().rstrip()
suffix_array, rank = get_suffix_array_and_rank(word)
lcp = get_lcp(word, suffix_array, rank)

print(" ".join(map(lambda x: str(x + 1), suffix_array)))
print(" ".join(map(str, lcp)))
