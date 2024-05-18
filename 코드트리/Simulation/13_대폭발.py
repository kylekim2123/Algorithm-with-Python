n, m, r, c = map(int, input().split())
board = [[-1] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
board[r - 1][c - 1] = 0

for t in range(1, m + 1):
    for x in range(n):
        for y in range(n):
            if board[x][y] == -1 or board[x][y] == t:
                continue

            for i in range(4):
                nx = x + dx[i] * (2 ** (t - 1))
                ny = y + dy[i] * (2 ** (t - 1))

                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                    board[nx][ny] = t

print(sum(board[x][y] > -1 for x in range(n) for y in range(n)))
