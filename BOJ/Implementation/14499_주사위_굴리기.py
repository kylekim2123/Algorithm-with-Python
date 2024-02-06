# 골드 4

import sys

input = sys.stdin.readline


def move_dice(direction):
    global dice
    up, down, left, right, front, back = dice

    if direction == 0:
        dice = [left, right, down, up, front, back]
    elif direction == 1:
        dice = [right, left, up, down, front, back]
    elif direction == 2:
        dice = [front, back, left, right, down, up]
    else:
        dice = [back, front, left, right, up, down]


n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int, input().split()))
dice = [0] * 6  # 상하좌우앞뒤
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]  # 우좌상하

for direction in directions:
    direction -= 1
    nx, ny = x + dx[direction], y + dy[direction]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    move_dice(direction)

    if board[nx][ny] == 0:
        board[nx][ny] = dice[1]
    else:
        dice[1] = board[nx][ny]
        board[nx][ny] = 0

    x, y = nx, ny

    print(dice[0])
