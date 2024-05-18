# 1780. 종이의 개수 (실버2)

import sys

input = sys.stdin.readline


def is_same(sx, sy, ex, ey):
    for i in range(sx, ex):
        for j in range(sy, ey):
            if paper[i][j] != paper[sx][sy]:
                return False
    return True


def cut(sx, sy, ex, ey):
    if is_same(sx, sy, ex, ey):
        result[paper[sx][sy] + 1] += 1
        return

    jump = (ex - sx) // 3

    for i in range(sx, ex, jump):
        for j in range(sy, ey, jump):
            cut(i, j, i + jump, j + jump)


n = int(input().rstrip())
result = [0, 0, 0]
paper = [list(map(int, input().split())) for _ in range(n)]
cut(0, 0, n, n)
print(*result, sep="\n")
