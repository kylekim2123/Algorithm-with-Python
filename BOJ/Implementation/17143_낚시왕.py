# 골드 1

import sys

input = sys.stdin.readline

r, c, m = map(int, input().split())
board = [[[] for _ in range(c)] for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]  # 상하우좌
sharks = set()
total = 0

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    board[x - 1][y - 1] = [s, d - 1, z]
    sharks.add((x - 1, y - 1))

# 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
for king in range(c):
    # 2. 낚시왕의 열에 있는 상어 중, 땅과 제일 가까운 상어를 잡는다. 상어는 격자판에서 사라진다.
    for x in range(r):
        if board[x][king]:
            total += board[x][king][2]
            sharks.remove((x, king))
            board[x][king] = []
            break

    if king == c - 1:
        break

    # 3. 상어가 이동한다.
    next_board = [[[] for _ in range(c)] for _ in range(r)]
    next_sharks = set()

    for x, y in sharks:
        s, d, z = board[x][y]

        for _ in range(s):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                x, y = nx, ny
            else:
                d += 1 if d == 0 or d == 2 else -1
                x += dx[d]
                y += dy[d]

        if not next_board[x][y] or next_board[x][y][2] < z:
            next_board[x][y] = [s, d, z]
            next_sharks.add((x, y))

    board = next_board
    sharks = next_sharks

print(total)
