# 골드 3

import sys

input = sys.stdin.readline

n = int(input())
board = [[0] * 101 for _ in range(101)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]  # 우상좌하
total = 0

for _ in range(n):
    x, y, d, g = map(int, input().split())
    nx, ny = x + dx[d], y + dy[d]
    board[y][x] = board[ny][nx] = 1
    prev_directions = [d]

    for _ in range(g):
        for prev_direction in prev_directions[::-1]:
            next_direction = (prev_direction + 1) % 4
            nx += dx[next_direction]
            ny += dy[next_direction]
            board[ny][nx] = 1
            prev_directions.append(next_direction)

for i in range(100):
    for j in range(100):
        if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] == 1:
            total += 1

print(total)
