# 7562. 나이트의 이동 (실버2)

from collections import deque

# 나이트의 움직임 8가지
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

def bfs(x, y):
    queue = deque([(x, y)])
    board[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1 # bfs의 depth
                if nx == x2 and ny == y2:
                    return

for _ in range(int(input())):
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    board = [[0]*n for _ in range(n)]
    bfs(x1, y1)
    print(board[x2][y2]-1)