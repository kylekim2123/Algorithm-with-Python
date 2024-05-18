def move(length):
    global x, y, direction, temp

    for _ in range(length):
        nx, ny = x + dx[direction], y + dy[direction]
        board[nx][ny], temp = temp, board[nx][ny]
        x, y = nx, ny

    direction += d

    if direction < 0:
        direction = 3
    elif direction > 3:
        direction = 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
x, y, m1, m2, m3, m4, d = map(int, input().split())
dx, dy = [-1, -1, 1, 1], [1, -1, -1, 1]  # 우상, 좌상, 좌하, 우하
x -= 1
y -= 1

d = 1 if d == 0 else -1
direction = 0 if d == 1 else 1

if d == -1:
    m1, m2, m3, m4 = m4, m3, m2, m1

temp = board[x][y]

move(m1)
move(m2)
move(m3)
move(m4)

for line in board:
    print(*line)
