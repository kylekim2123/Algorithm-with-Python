import sys

input = sys.stdin.readline


def recursion(depth, choices):
    global max_counts

    if len(choices) + (n - depth) <= max_counts:
        return

    if depth == n:
        max_counts = max(max_counts, len(choices))
        return

    recursion(depth + 1, choices)

    x3, x4 = lines[depth]

    for x1, x2 in choices:
        if x1 <= x3 <= x2 or x1 <= x4 <= x2 or x3 <= x1 <= x4 or x3 <= x2 <= x4:
            return

    recursion(depth + 1, choices + [lines[depth]])


n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
max_counts = 1

recursion(0, [])

print(max_counts)
