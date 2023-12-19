# 상 하 좌 우 좌상 우상 좌하 우하
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def play_othello(board, m):
    for _ in range(m):
        y, x, color = map(int, input().split()) # 입력이 x,y가 반대로 들어오기 때문에 이렇게 입력 받는다.
        board[x][y] = color # 돌 놓은 자리 색칠
        for i in range(8): # 팔방으로 탐색
            nx, ny = x+dx[i], y+dy[i]
            changes = [] # "반대의 돌"이어서 색칠을 하게 되면, 해당 좌표를 기록
            while board[nx][ny] == 3 - color: # black은 1, white는 2이므로, 3에서 빼면 각각 "반대의 돌"을 의미
                changes.append((nx, ny)) # "반대의 돌"일 때 색칠 후보
                nx += dx[i]
                ny += dy[i]
                if board[nx][ny] == 0:
                    break # 그러나, 맞은편 끝에 자기와 같은 색의 돌이 없으면, 색칠 불가능
            else:
                for a, b in changes:
                    board[a][b] = color # 맞은편 끝에 같은 색의 돌이 있으면, 색칠

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    board = [[0]*(n+2) for _ in range(n+2)] # 보드 주변에 벽을 세운다
    half = n // 2
    board[half][half], board[half][half+1], board[half+1][half], board[half+1][half+1] = 2, 1, 1, 2 # 최초 돌 위치
    play_othello(board, m)

    # 오델로 게임이 끝난 후, 흑백 갯수 세기
    black, white = 0, 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print('#%s %s %s' % (t, black, white))
