n = int(input())
board = [[-1] * (n + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)] + [[-1] * (n + 2)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상, 우, 하, 좌
max_seconds = 2

for x in range(n + 2):
    for y in range(n + 2):
        if board[x][y] != -1:
            continue

        for k in range(4):
            sx, sy = x + dx[k], y + dy[k]

            if 0 <= sx < n + 2 and 0 <= sy < n + 2 and board[sx][sy] != -1:
                break

        i, j = sx, sy
        direction = k
        seconds = 1

        while board[i][j] != -1:
            if board[i][j] == 1:
                direction += 1 if direction == 0 or direction == 2 else -1
            elif board[i][j] == 2:
                direction += 1 if direction == 1 or direction == 3 else -1
                if direction > 3:
                    direction = 0
                elif direction < 0:
                    direction = 3

            seconds += 1
            i += dx[direction]
            j += dy[direction]

        max_seconds = max(max_seconds, seconds)

print(max_seconds)
