def dfs(x, y, total, direction):
    if direction == 3 and x - cx != y - cy:
        return

    if direction == 2 and x == cx:
        return

    if total > 0 and x == cx and y == cy:
        global max_total
        max_total = max(max_total, total)
        return

    total += board[x][y]

    nx, ny = x + dx[direction], y + dy[direction]
    if 0 <= nx < n and 0 <= ny < n:
        dfs(nx, ny, total, direction)

    direction += 1
    if direction <= 3:
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n:
            dfs(nx, ny, total, direction)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, 1, -1, -1], [-1, 1, 1, -1]  # 좌하, 우하, 우상, 좌상
max_total = 0

for cx in range(n - 1):
    for cy in range(1, n - 1):
        dfs(cx, cy, 0, 0)

print(max_total)
