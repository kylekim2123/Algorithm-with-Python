# 골드 2

import sys

input = sys.stdin.readline


def up(board):
    board = [list(line) for line in board]
    visited = [[False] * n for _ in range(n)]

    for x in range(1, n):
        for y in range(n):
            if board[x][y] == 0:
                continue

            tx = x
            nx = x - 1

            while nx >= 0 and board[nx][y] == 0:
                board[nx][y] = board[tx][y]
                board[tx][y] = 0
                nx -= 1
                tx -= 1

            if nx >= 0 and board[tx][y] == board[nx][y] and not visited[nx][y]:
                board[nx][y] += board[tx][y]
                board[tx][y] = 0
                visited[nx][y] = True
                continue

    return board


def down(board):
    board = [list(line) for line in board]
    visited = [[False] * n for _ in range(n)]

    for x in range(n - 2, -1, -1):
        for y in range(n):
            if board[x][y] == 0:
                continue

            tx = x
            nx = x + 1

            while nx < n and board[nx][y] == 0:
                board[nx][y] = board[tx][y]
                board[tx][y] = 0
                nx += 1
                tx += 1

            if nx < n and board[tx][y] == board[nx][y] and not visited[nx][y]:
                board[nx][y] += board[tx][y]
                board[tx][y] = 0
                visited[nx][y] = True
                continue

    return board


def left(board):
    board = [list(line) for line in board]
    visited = [[False] * n for _ in range(n)]

    for y in range(1, n):
        for x in range(n):
            if board[x][y] == 0:
                continue

            ty = y
            ny = y - 1

            while ny >= 0 and board[x][ny] == 0:
                board[x][ny] = board[x][ty]
                board[x][ty] = 0
                ny -= 1
                ty -= 1

            if ny >= 0 and board[x][ty] == board[x][ny] and not visited[x][ny]:
                board[x][ny] += board[x][ty]
                board[x][ty] = 0
                visited[x][ny] = True
                continue

    return board


def right(board):
    board = [list(line) for line in board]
    visited = [[False] * n for _ in range(n)]

    for y in range(n - 2, -1, -1):
        for x in range(n):
            if board[x][y] == 0:
                continue

            ty = y
            ny = y + 1

            while ny < n and board[x][ny] == 0:
                board[x][ny] = board[x][ty]
                board[x][ty] = 0
                ny += 1
                ty += 1

            if ny < n and board[x][ty] == board[x][ny] and not visited[x][ny]:
                board[x][ny] += board[x][ty]
                board[x][ty] = 0
                visited[x][ny] = True
                continue

    return board


def play(depth, board):
    if depth == 5:
        global max_number
        max_number = max(max_number, max(map(max, board)))

        return

    depth += 1

    for i in range(4):
        play(depth, direction[i](board))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [up, down, left, right]
max_number = 0

play(0, board)

print(max_number)
