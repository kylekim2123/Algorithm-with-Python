T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(n)]
    max_total = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            total = 0
            for x in range(i, i+m):
                for y in range(j, j+m):
                    total += area[x][y]
            if total > max_total:
                max_total = total
    print('#%s %s' % (t, max_total))