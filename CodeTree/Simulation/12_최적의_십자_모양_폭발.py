def cross_explode(board, x, y):
    for i in range(4):
        for j in range(1, board[x][y]):
            nx, ny = x + dx[i] * j, y + dy[i] * j

            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 0

    board[x][y] = 0


def drop(board):
    for y in range(n):
        temp = [board[x][y] for x in range(n) if board[x][y] > 0]
        i = 0

        for x in range(n):
            if x < n - len(temp):
                board[x][y] = 0
            else:
                board[x][y] = temp[i]
                i += 1


def count_pairs(board):
    dx, dy = [0, 1], [1, 0]
    counts = 0

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                continue

            for i in range(2):
                nx, ny = x + dx[i], y + dy[i]

                if nx < n and ny < n and board[x][y] == board[nx][ny]:
                    counts += 1

    return counts


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_pairs = 0

for x in range(n):
    for y in range(n):
        copy_board = list(map(list, board))

        cross_explode(copy_board, x, y)
        drop(copy_board)

        max_pairs = max(max_pairs, count_pairs(copy_board))

print(max_pairs)
