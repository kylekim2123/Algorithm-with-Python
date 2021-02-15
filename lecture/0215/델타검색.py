T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(5)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    total = 0
    for r in range(5):
        for c in range(5):
            for i in range(4):
                next_r = r + dr[i]
                next_c = c + dc[i]
                if 0 <= next_r < 5 and 0 <= next_c < 5:
                    sub = arr[r][c] - arr[next_r][next_c]
                    if sub < 0:
                        sub = -sub
                    total += sub

    print('#%s %s' % (t, total))