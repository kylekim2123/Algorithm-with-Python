WALL = -1
EMPTY = 0
DIRECTION_MAX_INDEX = 3

dr = (0, 1, 0, -1) # 우하좌상
dc = (1, 0, -1, 0)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    snail = [[WALL] * (n+2) for _ in range(n+2)] # 달팽이 숫자 주변에 가벽을 세우기 위해 n+2 범위 사용
    for i in range(1, n+1):
        for j in range(1, n+1):
            snail[i][j] = EMPTY # 달팽이 숫자가 들어가는 부분은 0으로 비움

    r, c = 1, 1
    direction = 0 # 델타의 인덱스
    for number in range(1, (n**2)+1):
        snail[r][c] = number
        if snail[r + dr[direction]][c + dc[direction]] != EMPTY:
            direction += 1 # 다음 공간이 비어있지 않다면 방향을 바꿈
            if direction > DIRECTION_MAX_INDEX:
                direction = 0 # 델타의 인덱스가 max를 넘어가면 0으로 초기화
        r += dr[direction]
        c += dc[direction]

    print('#%s' % t)
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(snail[i][j], end=' ')
        print()
