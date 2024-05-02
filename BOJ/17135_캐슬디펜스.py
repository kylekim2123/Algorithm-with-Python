# 골드 3

import sys
from itertools import combinations

input = sys.stdin.readline
EMPTY, ENEMY = 0, 1


def get_reachable_range(x1, y1):
    reachable_range = []

    for x2 in range(n):
        for y2 in range(m):
            distance = abs(x1 - x2) + abs(y1 - y2)
            if distance <= d:
                reachable_range.append((distance, x2, y2))

    reachable_range.sort(key=lambda value: (value[0], value[2]))

    return reachable_range


def is_game_over(board):
    return sum(map(sum, board)) > 0


def kill_enemies(board, archer_ys):
    killed_enemies = set()

    for archer_y in archer_ys:
        for _, x, y in reachable_ranges[archer_y]:
            if board[x][y] == ENEMY:
                killed_enemies.add((x, y))
                break

    for x, y in killed_enemies:
        board[x][y] = EMPTY

    return len(killed_enemies)


def go_down(board):
    for y in range(m):
        for x in range(n - 1, 0, -1):
            board[x][y] = board[x - 1][y]

    board[0] = [0] * m


def play_castle_defense(archer_ys):
    global max_total
    temp_board = [list(line) for line in board]
    total = 0

    while is_game_over(temp_board):
        total += kill_enemies(temp_board, archer_ys)
        go_down(temp_board)

    max_total = max(max_total, total)


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
reachable_ranges = [get_reachable_range(n, y) for y in range(m)]
max_total = 0

for archer_ys in combinations(range(m), 3):
    play_castle_defense(archer_ys)

print(max_total)
