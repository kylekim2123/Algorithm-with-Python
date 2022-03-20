# 1913. 달팽이 (실버4)

n, k = int(input()), int(input())
board = [[0] * n for _ in range(n)]

x, y, direction = 0, 0, 0
dxy = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}  # 하, 우, 상, 좌

for i in range(n * n, 0, -1):
    if i == k:
        kx, ky = x + 1, y + 1

    board[x][y] = i
    dx, dy = dxy[direction]
    nx, ny = x + dx, y + dy

    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
        x, y = nx, ny
    else:
        direction = (direction + 1) % 4
        dx, dy = dxy[direction]
        x, y = x + dx, y + dy

for line in board:
    print(*line)
print(kx, ky)
