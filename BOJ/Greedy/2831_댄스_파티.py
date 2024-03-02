# 골드 4

import sys

input = sys.stdin.readline


def find(plus, minus):
    i, j, total = 0, 0, 0

    while i < len(plus) and j < len(minus):
        if plus[i] < minus[j]:
            total += 1
            i += 1

        j += 1

    return total


n = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))

men_plus = sorted(m for m in men if m > 0)
men_minus = sorted(-m for m in men if m < 0)
women_plus = sorted(w for w in women if w > 0)
women_minus = sorted(-w for w in women if w < 0)

print(find(men_plus, women_minus) + find(women_plus, men_minus))
