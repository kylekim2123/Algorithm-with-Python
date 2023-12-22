def is_transmissible(prev, now):
    for i in range(m):
        if board[prev][i] == board[now][i]:
            return True

    return False


def blow(prev, now, direction):
    if now < 0 or now >= n or not is_transmissible(prev, now):
        return

    if direction == "L":
        board[now] = board[now][1:] + [board[now][0]]
        direction = "R"
    else:
        board[now] = [board[now][-1]] + board[now][:-1]
        direction = "L"

    if now < prev:
        blow(now, now - 1, direction)
    else:
        blow(now, now + 1, direction)


n, m, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for _ in range(q):
    r, d = input().split()
    r = int(r) - 1

    if d == "L":
        board[r] = [board[r][-1]] + board[r][:-1]
    else:
        board[r] = board[r][1:] + [board[r][0]]

    blow(r, r - 1, d)
    blow(r, r + 1, d)

for line in board:
    print(*line)
