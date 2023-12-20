from collections import deque


def bfs(x, y):
    visited = [[0] * n for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = 1
    total = board[x][y]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                total += board[nx][ny]

                if visited[nx][ny] == k + 1:
                    continue

                queue.append((nx, ny))

    return total


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_total = 1 if sum(map(sum, board)) > 0 and m >= 1 else 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for k in range(1, n + 1):
    cost = k * k + (k + 1) * (k + 1)

    for i in range(n):
        for j in range(n):
            total = bfs(i, j)

            if total * m >= cost:
                max_total = max(max_total, total)

print(max_total)
