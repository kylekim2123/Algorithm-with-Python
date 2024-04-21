# 플래티넘 2

import sys

input = sys.stdin.readline
DX, DY = [-1, 1, 0, 0], [0, 0, -1, 1]
MAX = 99999999


def find_x(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "X":
                return i, j


def convert_to_string(board):
    return "".join(["".join(line) for line in board])


def dfs(x, y, depth, limit, board, movements):
    # 제한 보다 많이 오면 백트래킹
    if depth > limit:
        return

    key = convert_to_string(board)

    # 이미 방문한 적이 있고, 이전보다 효율적이지 않다면 백트래킹
    if key in movements and movements[key] <= depth:
        return

    movements[key] = min(movements.get(key, depth), depth)

    for i in range(4):
        nx, ny = x + DX[i], y + DY[i]

        if 0 <= nx < size and 0 <= ny < size:
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]  # 변경
            dfs(nx, ny, depth + 1, limit, board, movements)
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]  # 복구


while True:
    try:
        _, size, counts = input().split()
        size, counts = int(size), int(counts)

        # 시작 전 보드
        origin_board = [input().split() for _ in range(size)]
        sx, sy = find_x(origin_board)
        origin_movements = {}
        origin_movement_count = counts // 2

        # 완료 후 보드
        target_board = [input().split() for _ in range(size)]
        ex, ey = find_x(target_board)
        target_movements = {}
        target_movement_count = counts // 2 if counts % 2 == 0 else counts // 2 + 1

        _ = input()

        # 서로 counts의 반만큼 따로 움직여서 board가 동일해지는 구간의 최소 거리를 구함
        dfs(sx, sy, 0, origin_movement_count, origin_board, origin_movements)
        dfs(ex, ey, 0, target_movement_count, target_board, target_movements)

        # 딕셔너리에서 같은 모양의 board를 찾아 최소 거리를 더한 후, counts내로 들어왔는지 확인하고 결과 출력
        min_dist = MAX

        for board, dist in origin_movements.items():
            if board not in target_movements:
                continue

            min_dist = min(min_dist, dist + target_movements[board])

        if min_dist == MAX:
            print(f"NOT SOLVABLE WITHIN {counts} MOVES\n")
        else:
            print(f"SOLVABLE WITHIN {min_dist} MOVES\n")

    except ValueError:
        break
