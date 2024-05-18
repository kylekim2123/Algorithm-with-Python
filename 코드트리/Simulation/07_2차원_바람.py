n, m, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 우, 하, 좌, 상

for _ in range(q):
    r1, c1, r2, c2 = map(lambda x: int(x) - 1, input().split())

    # 1. 테두리 회전
    length = ((r2 - r1 + 1) + (c2 - c1 + 1)) * 2 - 4
    temp = board[r1][c1]
    x, y = r1, c1
    direction = 0

    for _ in range(length):
        nx, ny = x + dx[direction], y + dy[direction]

        if nx < r1 or nx > r2 or ny < c1 or ny > c2:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]

        board[nx][ny], temp = temp, board[nx][ny]
        x, y = nx, ny

    # 2. 평균값 계산
    temp = [[0] * m for _ in range(n)]

    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            total = board[x][y]
            counts = 1

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    total += board[nx][ny]
                    counts += 1

            temp[x][y] = total // counts

    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            board[x][y] = temp[x][y]

for line in board:
    print(*line)
