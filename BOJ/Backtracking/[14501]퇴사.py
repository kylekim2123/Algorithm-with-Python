# 14501. 퇴사 (실버3)

import sys

input = sys.stdin.readline


def discuss(index, total, last_benefit):
    if index >= n:
        global max_total
        total += last_benefit if index == n else 0
        max_total = max(max_total, total)
        return

    total += last_benefit
    discuss(index + 1, total, 0)
    discuss(index + board[index][0], total, board[index][1])


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_total = 0

discuss(0, 0, 0)

print(max_total)
