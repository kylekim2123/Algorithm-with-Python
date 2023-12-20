n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_total = 0

delta = [
    [(0, 1), (1, 0)],
    [(0, -1), (1, 0)],
    [(-1, 0), (0, 1)],
    [(-1, 0), (0, -1)],
    [(0, -1), (0, 1)],
    [(-1, 0), (1, 0)]
]

for x in range(n):
    for y in range(m):
        for dxy in delta:
            total = board[x][y]

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    total += board[nx][ny]

            max_total = max(max_total, total)

print(max_total)
