def choice(depth, total):
    global max_total
    if depth >= n:
        max_total = max(max_total, total)
        return
    for i in range(n):
        next_total = total * p[depth][i]
        if not is_chosen[i] and next_total > max_total:
            is_chosen[i] = 1
            choice(depth+1, next_total)
            is_chosen[i] = 0

for t in range(1, int(input())+1):
    n = int(input())
    p = [list(map(lambda x: float(x)/100.0, input().split())) for _ in range(n)]
    is_chosen = [0] * n
    max_total = 0
    choice(0, 1)
    print('#{} {:.6f}'.format(t, max_total*100.0))
