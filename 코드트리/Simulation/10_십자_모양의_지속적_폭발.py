n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상, 하, 좌, 우

for _ in range(m):
    y = int(input()) - 1

    for x in range(n):
        if board[x][y] == 0:
            continue

        for i in range(4):
            for j in range(1, board[x][y]):
                nx, ny = x + dx[i] * j, y + dy[i] * j
                if 0 <= nx < n and 0 <= ny < n:
                    board[nx][ny] = 0

        board[x][y] = 0
        break

    for y in range(n):
        for x in range(n - 1, 0, -1):
            if board[x][y] == 0:
                board[x][y] = board[x - 1][y]
                board[x - 1][y] = 0

for line in board:
    print(*line)
