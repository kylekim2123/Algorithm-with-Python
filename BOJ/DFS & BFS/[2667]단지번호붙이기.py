# 2667. 단지번호붙이기 (실버1)

import sys
input = sys.stdin.readline

def dfs(x, y):
    global total
    board[x][y] = 0
    total += 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0:
            board[nx][ny] = 0
            dfs(nx, ny)


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = []

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            total = 0
            dfs(i, j)
            result.append(total)

print(len(result), *sorted(result), sep="\n")
