n, m, t, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
dxy = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

for order in range(m):
    r, c, d, v = input().split()
    r, c = int(r) - 1, int(c) - 1
    board[r][c].append((int(v), order, dxy[d]))

for _ in range(t):
    temp = [[[] for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            for v, order, delta in board[x][y]:
                sx, sy = x, y
                dx, dy = delta

                for _ in range(v):
                    nx, ny = sx + dx, sy + dy

                    if 0 <= nx < n and 0 <= ny < n:
                        sx, sy = nx, ny
                    else:
                        dx *= -1
                        dy *= -1
                        sx += dx
                        sy += dy

                temp[sx][sy].append((v, order, (dx, dy)))

    for x in range(n):
        for y in range(n):
            board[x][y] = sorted(temp[x][y], reverse=True)[:k]

print(sum(sum(map(len, line)) for line in board))
