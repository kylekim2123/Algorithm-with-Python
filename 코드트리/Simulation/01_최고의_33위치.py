n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_total = 0

for i in range(n - 2):
    for j in range(n - 2):
        total = sum(board[r][c] for r in range(i, i + 3) for c in range(j, j + 3))
        max_total = max(max_total, total)

print(max_total)
