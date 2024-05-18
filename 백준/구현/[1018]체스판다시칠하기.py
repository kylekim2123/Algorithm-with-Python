# 1018. 체스판 다시 칠하기 (실버5)


def paint_squares(x, y, board):
    check = board[x][y]
    count = 0

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if board[i][j] != check:
                count += 1
                if count >= min_count:
                    return min_count
            check = switching_color[check] if j < y + 7 else check
    return count


n, m = map(int, input().split())
origin_board = [input() for _ in range(n)]
switching_color = {"W": "B", "B": "W"}
min_count = n * m

for i in range(0, n - 7):
    for j in range(0, m - 7):
        for _ in range(4):
            min_count = paint_squares(i, j, origin_board)
            origin_board = [line[::-1] for line in zip(*origin_board)]  # rotate
            i, j = j, i

print(min_count)
