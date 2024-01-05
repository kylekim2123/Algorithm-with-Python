import sys
from collections import deque

input = sys.stdin.readline
OUT_WATER, ICE, IN_WATER = 2, 1, 0


def is_all_melted():
    for i in range(n):
        for j in range(m):
            if board[i][j] == ICE:
                return False

    return True


def mark_out_water():
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] != ICE:
                visited[nx][ny] = True
                board[nx][ny] = OUT_WATER
                queue.append((nx, ny))


def melt():
    visited = [[False] * m for _ in range(n)]
    melting_size = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == ICE:
                visited[i][j] = True

                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and board[ni][nj] == OUT_WATER:
                        board[i][j] = OUT_WATER
                        melting_size += 1
                        break

    return melting_size


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
seconds = 0

while not is_all_melted():
    seconds += 1
    mark_out_water()
    last_melting_size = melt()

print(seconds, last_melting_size)
