def get_exploded_x(y):
    exploded_x = []
    x = 0
    counts = 0
    standard = board[x][y]

    while x < n:
        if board[x][y] == 0:
            x += 1
            if x < n:
                standard = board[x][y]
            continue

        if standard == board[x][y]:
            x += 1
            counts += 1
        else:
            if m <= counts:
                for i in range(x - counts, x):
                    exploded_x.append(i)

            standard = board[x][y]
            counts = 0

    if m <= counts:
        for i in range(n - counts, n):
            exploded_x.append(i)

    return exploded_x


def line_explode(exploded_x, y):
    for x in exploded_x:
        board[x][y] = 0


def drop(y):
    temp = [board[x][y] for x in range(n) if board[x][y] > 0]
    i = 0

    for x in range(n):
        if x < n - len(temp):
            board[x][y] = 0
        else:
            board[x][y] = temp[i]
            i += 1


def bomb():
    for y in range(n):
        while True:
            exploded_x = get_exploded_x(y)

            if not exploded_x:
                break

            line_explode(exploded_x, y)
            drop(y)


def rotate():
    global board
    board = [list(line[::-1]) for line in zip(*board)]


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for _ in range(k):
    bomb()
    rotate()
    for y in range(n):
        drop(y)

bomb()

print(sum(board[x][y] > 0 for x in range(n) for y in range(n)))
