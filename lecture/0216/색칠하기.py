# 빨간색 혹은 파란색 사각형 범위만큼 칠하기
def paint_color(map_area):
    r1, c1, r2, c2, color = map(int, input().split())
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if map_area[i][j] == color: # 이미 같은 색으로 칠해져 있으면 패스
                continue
            elif map_area[i][j] == EMPTY: # 빈 공간인 경우 해당 색으로 칠함
                map_area[i][j] = color
            else:
                map_area[i][j] = PURPLE # 다른 색인 경우 보라색으로 변경


# 보라색 영역 세기
def count_purple(map_area):
    count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if map_area[i][j] == PURPLE:
                count += 1
    return count


SIZE = 10
EMPTY = 0
PURPLE = 3
T = int(input())
for t in range(1, T+1):
    area = [[EMPTY] * SIZE for _ in range(SIZE)]
    n = int(input())
    for _ in range(n):
        paint_color(area)
    print('#%s %s' % (t, count_purple(area)))
