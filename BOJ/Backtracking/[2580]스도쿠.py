# 2580. 스도쿠 (골드4)

import sys

input = sys.stdin.readline


def get_candidates(x, y):
    row = set(sudoku[x])
    col = set(sudoku[i][y] for i in range(9))
    block = set(
        sudoku[i][j]
        for i in range(standard[x], standard[x] + 3)
        for j in range(standard[y], standard[y] + 3)
    )

    candidates = set(range(10)) - row - col - block
    if 0 in candidates:
        candidates.remove(0)

    return candidates


def play(depth):
    if depth == len(spaces):
        for line in sudoku:
            print(*line)
        sys.exit(0)

    x, y = spaces[depth]
    for candidate in get_candidates(x, y):
        sudoku[x][y] = candidate
        play(depth + 1)
        sudoku[x][y] = 0


sudoku = []
spaces = []
standard = [0, 0, 0, 3, 3, 3, 6, 6, 6]

for i in range(9):
    line = list(map(int, input().split()))
    sudoku.append(line)
    for j in range(9):
        if line[j] == 0:
            spaces.append((i, j))

play(0)
