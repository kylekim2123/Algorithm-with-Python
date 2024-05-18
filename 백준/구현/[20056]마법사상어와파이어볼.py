# 20056. 마법사 상어와 파이어볼 (골드4)

import sys

input = sys.stdin.readline
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
fire = [list(map(int, input().split())) for _ in range(m)]
board = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(k):
    for x, y, mass, speed, direction in fire:
        nx = (x - 1 + dx[direction] * speed) % n
        ny = (y - 1 + dy[direction] * speed) % n
        board[nx][ny].append((mass, speed, direction))

    temp = []
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                continue

            if len(board[i][j]) == 1:
                temp.append((i + 1, j + 1) + tuple(board[i][j][0]))
                board[i][j] = []
                continue

            new_mass = sum(info[0] for info in board[i][j]) // 5
            new_speed = sum(info[1] for info in board[i][j]) // len(board[i][j])
            if len(set(info[2] % 2 for info in board[i][j])) == 1:
                new_directions = (0, 2, 4, 6)
            else:
                new_directions = (1, 3, 5, 7)

            if new_mass > 0 and new_speed > 0:
                for new_direction in new_directions:
                    temp.append((i + 1, j + 1, new_mass, new_speed, new_direction))

            board[i][j] = []

    fire = temp

print(sum(info[2] for info in fire))
