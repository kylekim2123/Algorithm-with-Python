def move(x, y, total):
    if x == n-1 and y == n-1:
        global min_total
        min_total = min(min_total, total)
        return
    if y + 1 < n:
        move(x, y+1, total+numbers[x][y+1])
    if x + 1 < n:
        move(x+1, y, total+numbers[x+1][y])

for t in range(1, int(input())+1):
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(n)]
    min_total = 13 * 13 * 10
    move(0, 0, numbers[0][0])
    print('#%s %s' % (t, min_total))