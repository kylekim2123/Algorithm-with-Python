SIZE = 10
EMPTY = 0
PURPLE = 3
T = int(input())
for t in range(1, T+1):
    area = [[EMPTY] * SIZE for _ in range(SIZE)]
    n = int(input())
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if area[i][j] == color:
                    continue
                elif area[i][j] == EMPTY:
                    area[i][j] = color
                else:
                    area[i][j] = PURPLE

    count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if area[i][j] == PURPLE:
                count += 1
    print('#%s %s' % (t, count))
