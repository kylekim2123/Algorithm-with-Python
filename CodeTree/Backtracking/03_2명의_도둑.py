import sys

input = sys.stdin.readline


def pick(depth, weights, choices):
    if sum(choices) > c:
        return 0

    if depth == m:
        return sum(map(lambda x: x * x, choices))

    return max(pick(depth + 1, weights, choices + [weights[depth]]), pick(depth + 1, weights, choices))


n, m, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_value = 0

for x1 in range(n):
    for y1 in range(n - m + 1):
        v1 = pick(0, board[x1][y1: y1 + m], [])

        for x2 in range(x1, n):
            for y2 in range(n - m + 1):
                if x1 == x2 and y2 < y1 + m:
                    continue

                v2 = pick(0, board[x2][y2: y2 + m], [])
                max_value = max(max_value, v1 + v2)

print(max_value)
