# 20058. 마법사 상어와 파이어스톰 (골드4)

import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

8
def get_rotated_board():
    rotated_board = [[0] * n for _ in range(n)]

    for i in range(0, n, l):
        for j in range(0, n, l):
            for x in range(l):
                for y in range(l):
                    rotated_board[i + y][j + l - x - 1] = board[i + x][j + y]

    return rotated_board


def melt():
    melts = []

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                adj = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] > 0:
                        adj += 1
                if adj < 3:
                    melts.append((i, j))

    for i, j in melts:
        board[i][j] -= 1


def bfs(x, y):
    total = 0
    visited[x][y] = True
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        total += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return total


n, _ = map(int, input().split())
n = 2 ** n
board = [list(map(int, input().split())) for _ in range(n)]

for l in map(int, input().split()):
    l = 2 ** l

    # 1. 부분 격자 90도 회전
    if l > 1:
        board = get_rotated_board()

    # 2. 얼음 줄이기
    melt()

# 3. BFS - 가장 큰 덩어리의 칸 개수 구하기
visited = [[False] * n for _ in range(n)]
max_total = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] > 0:
            max_total = max(max_total, bfs(i, j))

# 4. 남아있는 얼음 합, 가장 큰 덩어리의 칸 개수 출력
print(sum(map(sum, board)))
print(max_total)
