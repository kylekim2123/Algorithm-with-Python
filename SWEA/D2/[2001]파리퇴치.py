# 2001. 파리 퇴치

for t in range(1, int(input()) + 1):
    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]

    squares = [list(map(int, input().split())) for _ in range(n)]
    max_kill = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for k in range(m):
                total += sum(squares[i + k][j:j + m])
            max_kill = max(max_kill, total)

    print(f'#{t} {max_kill}')