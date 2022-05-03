# 3190. 뱀 (골드5)

import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상, 우, 하, 좌


def get_play_time():
    seconds = 0
    now = 1  # 시작 방향(우)
    snake = deque([(0, 0)])
    x, c = changes.popleft()

    while True:
        seconds += 1
        i, j = snake[-1]
        ni, nj = i + dx[now], j + dy[now]

        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != 1:
            snake.append((ni, nj))
            if board[ni][nj] == 0:
                tail_i, tail_j = snake.popleft()
                board[tail_i][tail_j] = 0
            board[ni][nj] = 1
        else:
            return seconds

        if seconds == x:
            if c == "L":
                now -= 1
                if now < 0:
                    now = 3
            else:
                now += 1
                if now > 3:
                    now = 0

            if changes:
                x, c = changes.popleft()
            else:
                x = 100


n, k = int(input().rstrip()), int(input().rstrip())
board = [[0] * n for _ in range(n)]
board[0][0] = 1  # 최초의 뱀 위치

for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 2  # 사과 위치

changes = deque()  # 방향 전환 정보
for _ in range(int(input().rstrip())):
    x, c = input().split()
    changes.append((int(x), c))

print(get_play_time())
