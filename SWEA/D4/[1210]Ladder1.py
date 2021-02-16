# 1210. Ladder 1

def change_direction():
    left, right = x-1, x+1
    if left < 0:
        if ladders[y][right] == 1:
            return 2
    elif right >= SIZE:
        if ladders[y][left] == 1:
            return 0
    else:
        if ladders[y][right] == 1:
            return 2
        elif ladders[y][left] == 1:
            return 0
    return 1

dx = [-1, 0, 1] # 좌 상 우
dy = [0, -1, 0]
SIZE = 100
for _ in range(1, 11):
    t = int(input())
    ladders = [list(map(int, input().split())) for _ in range(SIZE)]

    for i in range(SIZE):
        if ladders[SIZE-1][i] == 2:
            x = i
            break
    y = SIZE-1

    direction = 1
    while y > 0:
        if direction == 1:
            direction = change_direction()
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if (next_x < 0) or (next_x >= SIZE) or (ladders[next_y][next_x] == 0):
            direction = 1
            y -= 1
        else:
            x, y = next_x, next_y

    print('#%s %s' % (t, x))