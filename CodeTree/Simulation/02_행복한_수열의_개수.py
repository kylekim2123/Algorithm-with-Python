def get_happy_sequence(board):
    happy_sequences = 0

    for i in range(n):
        for start in range(n):
            total = 1

            for end in range(start + 1, n):
                if board[i][start] != board[i][end]:
                    break
                total += 1

            if total >= m:
                happy_sequences += 1
                break

    return happy_sequences


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(get_happy_sequence(board) + get_happy_sequence(list(zip(*board))))
