# 상 하 좌 우 좌상 우상 좌하 우하
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def play_othello(board, m):
    for _ in range(m):
        y, x, color = map(int, input().split())
        board[x][y] = color
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            changes = []
            while board[nx][ny] == 3 - color:
                changes.append((nx, ny))
                nx += dx[i]
                ny += dy[i]
                if board[nx][ny] == 0:
                    break
            else:
                for a, b in changes:
                    board[a][b] = color

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    board = [[0]*(n+2) for _ in range(n+2)]
    half = n // 2
    board[half][half], board[half][half+1], board[half+1][half], board[half+1][half+1] = 2, 1, 1, 2
    play_othello(board, m)
    black, white = 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print('#%s %s %s' % (t, black, white))
