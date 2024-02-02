# 골드 1

import sys

input = sys.stdin.readline
SPACE, WALL, HOLE, RED, BLUE = ".", "#", "O", "R", "B"


def move(direction, x, y, board, color):
    cx, cy = x, y
    nx, ny = x + dx[direction], y + dy[direction]

    while board[nx][ny] == SPACE:
        board[cx][cy] = SPACE
        board[nx][ny] = color
        cx, cy = nx, ny
        nx += dx[direction]
        ny += dy[direction]

    return cx, cy, nx, ny


def play(moves, rx, ry, bx, by, board):
    global min_moves

    if moves >= min_moves:
        return

    for i in range(4):
        temp = [list(line) for line in board]

        if i == 0 and ry == by:
            first = RED if rx < bx else BLUE
        elif i == 1 and ry == by:
            first = RED if rx > bx else BLUE
        elif i == 2 and rx == bx:
            first = RED if ry < by else BLUE
        elif i == 3 and rx == bx:
            first = RED if ry > by else BLUE
        else:
            first = RED

        if first == RED:
            is_red_out = False
            crx, cry, nrx, nry = move(i, rx, ry, temp, RED)

            if temp[nrx][nry] == HOLE:
                is_red_out = True
                temp[crx][cry] = SPACE

            cbx, cby, nbx, nby = move(i, bx, by, temp, BLUE)

            if temp[nbx][nby] == HOLE:
                continue

            if is_red_out:
                min_moves = min(min_moves, moves)
                return
        else:
            cbx, cby, nbx, nby = move(i, bx, by, temp, BLUE)

            if temp[nbx][nby] == HOLE:
                continue

            crx, cry, nrx, nry = move(i, rx, ry, temp, RED)

            if temp[nrx][nry] == HOLE:
                min_moves = min(min_moves, moves)
                return

        if crx == rx and cry == ry and cbx == bx and cby == by:
            continue

        play(moves + 1, crx, cry, cbx, cby, temp)


n, m = map(int, input().split())
board = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
min_moves = 11

for i in range(n):
    line = list(input().rstrip())
    board.append(line)

    for j in range(m):
        if line[j] == RED:
            rx, ry = i, j
        elif line[j] == BLUE:
            bx, by = i, j

play(1, rx, ry, bx, by, board)

print(-1 if min_moves == 11 else min_moves)
