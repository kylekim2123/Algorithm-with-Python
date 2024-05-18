# 10157. 자리배정 (실버4)

c, r = map(int, input().split())
k = int(input())

if k > c * r:
    print(0)
else:
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 상우하좌
    board = [[0] * c for _ in range(r)]
    direction = 0
    x, y = r - 1, 0

    for i in range(1, c * r + 1):
        if i == k:
            print(y + 1, r - x)
            break

        board[x][y] = i
        nx, ny = x + dx[direction], y + dy[direction]

        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]
