n, m, t = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
dxy = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

for i in range(m):
    x, y, d, w = input().split()
    x, y = int(x) - 1, int(y) - 1
    board[x][y].append((i, int(w), dxy[d][0], dxy[d][1]))

for _ in range(t):
    temp = [[[] for _ in range(n)] for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if not board[x][y]:
                continue

            for i, w, dx, dy in board[x][y]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    temp[nx][ny].append((i, w, dx, dy))
                else:
                    dx *= -1
                    dy *= -1
                    temp[x][y].append((i, w, dx, dy))


    for x in range(n):
        for y in range(n):
            if not temp[x][y]:
                continue

            total_w = sum(w for _, w, _, _ in temp[x][y])
            i, _, dx, dy = max(temp[x][y], key=lambda bead: bead[0])
            temp[x][y] = [(i, total_w, dx, dy)]

    board = temp

counts = 0
max_w = 0

for x in range(n):
    for y in range(n):
        if not board[x][y]:
            continue

        counts += 1
        max_w = max(max_w, board[x][y][0][1])

print(counts, max_w)
