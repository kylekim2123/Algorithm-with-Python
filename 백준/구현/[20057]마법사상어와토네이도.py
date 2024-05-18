# 20057. 마법사 상어와 토네이도 (골드 3)

import sys

input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]  # 좌, 하, 우, 상
spread = [
    [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2),
     (1, -1), (1, 0), (1, 1), (2, 0)],  # 좌
    [(-1, -1), (-1, 1), (0, -2), (0, -1), (0, 1),
     (0, 2), (1, -1), (1, 1), (2, 0)],  # 하
    [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, 2),
     (1, -1), (1, 0), (1, 1), (2, 0)],  # 우
    [(-2, 0), (-1, -1), (-1, 1), (0, -2), (0, -1),
     (0, 1), (0, 2), (1, -1), (1, 1)]  # 상
]
rate = [
    [2, 10, 7, 1, 5, 10, 7, 1, 2],  # 좌
    [1, 1, 2, 7, 7, 2, 10, 10, 5],  # 하
    [2, 1, 7, 10, 5, 1, 7, 10, 2],  # 우
    [5, 10, 10, 2, 7, 7, 2, 1, 1]  # 상
]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
total = 0  # 격자 밖으로 나간 모래 양
direction = 0  # 최초 방향 : 좌
x, y = n // 2, n // 2  # 토네이토 시작 좌표
step, max_step, cnt = 0, 1, 0

for _ in range(n * n - 1):
    # 1. 토네이도 이동
    x += dx[direction]
    y += dy[direction]

    # 2. 모래 이동(비율)
    temp = 0  # 흩어지는 모래 양(남은 모래를 구하기 위함)

    for index, location in enumerate(spread[direction]):
        nx, ny = x + location[0], y + location[1]
        sand = int(board[x][y] * (rate[direction][index] / 100))
        temp += sand

        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] += sand
        else:
            total += sand

    # 3. 모래 이동(a)
    board[x][y] -= temp
    ax, ay = x + dx[direction], y + dy[direction]

    if 0 <= ax < n and 0 <= ay < n:
        board[ax][ay] += board[x][y]
    else:
        total += board[x][y]

    board[x][y] = 0

    # 4. 토네이도 방향 갱신
    step += 1

    if step >= max_step:
        direction = (direction + 1) % 4
        cnt += 1
        step = 0

    if cnt >= 2:
        max_step += 1
        cnt = 0

print(total)
