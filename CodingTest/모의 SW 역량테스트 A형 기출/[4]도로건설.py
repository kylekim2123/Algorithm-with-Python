# 도로 만들기 & 불가능한 경우 판별
def is_set_road(dxy):
    dx, dy = dxy
    nx, ny = x + dx, y + dy

    while 0 <= nx < h and 0 <= ny < w:
        if town[nx][ny] == 1:  # 도로 위에 집이 있으면 불가능
            return False
        road.append((nx, ny))
        nx += dx
        ny += dy

    return True


directions = [
    [(-1, 0), (1, 0)],  # 상하
    [(0, -1), (0, 1)],  # 좌우
    [(-1, -1), (1, 1)],  # 좌대각
    [(-1, 1), (1, -1)]  # 우대각
]

for t in range(1, int(input()) + 1):
    w, h = map(int, input().split())
    town, house = [], []
    result = 9999999

    for i in range(h):
        line = list(map(int, input().split()))
        town.append(line)
        for j in range(w):
            if line[j] == 1:
                house.append((i, j))

    for x in range(h):
        for y in range(w):
            if town[x][y] == 0:
                for k in range(4):
                    road = [(x, y)]

                    # 첫 방향 도로
                    if not is_set_road(directions[k][0]):
                        continue

                    # 반대 방향 도로
                    if not is_set_road(directions[k][1]):
                        continue

                    # 귀퉁이 부분에서 도로가 불가능한 특수 경우 판별
                    if len(road) <= 1:
                        continue

                    min_dists = [h + w] * len(house)  # 각 집에서 가장 가까운 도로와의 거리

                    for index, hxy in enumerate(house):
                        hx, hy = hxy
                        for rx, ry in road:
                            dist = abs(hx - rx) + abs(hy - ry)
                            min_dists[index] = min(dist, min_dists[index])

                    # 도로로부터 가장 멀리 떨어진 집과의 최소 거리
                    result = min(result, max(min_dists))

    if result == 9999999:
        result = -1

    print(f"#{t} {result}")
