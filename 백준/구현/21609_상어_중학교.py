# 골드 2

import sys
from collections import deque

input = sys.stdin.readline
EMPTY, BLACK, RAINBOW = -2, -1, 0


def bfs(x, y):
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    queue = deque([(x, y)])
    standard = board[x][y]
    normals = [(x, y)]
    rainbows = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (
                    board[nx][ny] == RAINBOW or board[nx][ny] == standard):
                if board[nx][ny] == RAINBOW:
                    rainbows.append((nx, ny))
                elif board[nx][ny] == standard:
                    normals.append((nx, ny))

                visited[nx][ny] = True
                queue.append((nx, ny))

    normals.sort()

    return rainbows, normals


def find_groups(board):
    checked = [[False] * n for _ in range(n)]
    groups = []

    for x in range(n):
        for y in range(n):
            if not checked[x][y] and board[x][y] > RAINBOW:
                checked[x][y] = True
                rainbows, normals = bfs(x, y)

                if len(normals) == 0 or len(normals) + len(rainbows) < 2:
                    continue

                for tx, ty in normals:
                    checked[tx][ty] = True

                groups.append(
                    (len(rainbows) + len(normals), len(rainbows), normals[0][0], normals[0][1], normals, rainbows))

    return sorted(groups, reverse=True)


def remove(blocks, rainbows, board):
    for x, y in blocks:
        board[x][y] = EMPTY

    for x, y in rainbows:
        board[x][y] = EMPTY

    global total
    total += (len(blocks) + len(rainbows)) ** 2


def drop(board):
    for y in range(n):
        last_empty_xy = []
        x = n - 1

        while x >= 0:
            if board[x][y] >= RAINBOW and not last_empty_xy:
                x -= 1
                continue

            if board[x][y] == BLACK:
                last_empty_xy = []
                x -= 1
                continue

            if board[x][y] == EMPTY:
                if not last_empty_xy:
                    last_empty_xy = [x, y]

                x -= 1
                continue

            ex, ey = last_empty_xy
            board[x][y], board[ex][ey] = board[ex][ey], board[x][y]
            last_empty_xy = []
            x = ex - 1


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
total = 0

while True:
    groups = find_groups(board)

    if not groups:
        break

    max_size_group = groups[0][4]
    max_size_rainbow = groups[0][5]
    remove(max_size_group, max_size_rainbow, board)

    drop(board)
    board = list(map(list, zip(*board)))[::-1]
    drop(board)

print(total)
