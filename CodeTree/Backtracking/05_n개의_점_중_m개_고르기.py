import sys

input = sys.stdin.readline


def get_farthest_dist(choices):
    farthest_dist = 0

    for i in range(len(choices) - 1):
        x1, y1 = choices[i]

        for j in range(i + 1, len(choices)):
            x2, y2 = choices[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            farthest_dist = max(farthest_dist, dist)

    return farthest_dist


def pick(depth, counts, choices):
    if counts == m:
        global min_dist
        min_dist = min(min_dist, get_farthest_dist(choices))

        return

    if depth == n or counts + (n - depth) < m:
        return

    pick(depth + 1, counts, choices)
    pick(depth + 1, counts + 1, choices + [points[depth]])


n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]
min_dist = 99999999

pick(0, 0, [])

print(min_dist)
