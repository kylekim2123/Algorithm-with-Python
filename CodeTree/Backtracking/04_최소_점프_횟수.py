import sys

input = sys.stdin.readline


def jump(depth, counts):
    if depth >= n - 1:
        global min_counts
        min_counts = min(counts, min_counts)

        return

    if numbers[depth] == 0:
        return

    for i in range(1, numbers[depth] + 1):
        jump(depth + i, counts + 1)


n = int(input())
numbers = list(map(int, input().split()))
min_counts = n

jump(0, 0)

print(-1 if min_counts == n else min_counts)
