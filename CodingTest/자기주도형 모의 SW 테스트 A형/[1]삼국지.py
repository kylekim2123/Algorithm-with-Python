dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def attack(country):
    area_change = [[0]*n for _ in range(n)]
    soldier_change = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if area[x][y] and area[x][y] != country:
                sum_soldiers = 0
                attack_xy = []
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < n and 0 <= ny < n and area[nx][ny] == country:
                        sum_soldiers += soldier[nx][ny]
                        attack_xy.append((nx, ny))
                if soldier[x][y] * 5 < sum_soldiers:
                    area_change[x][y] = country
                    for ax, ay in attack_xy:
                        soldier_change[x][y] += (soldier[ax][ay] // 4)
                        soldier_change[ax][ay] -= (soldier[ax][ay] // 4)

    for x in range(n):
        for y in range(n):
            if area_change[x][y]:
                area[x][y] = area_change[x][y]
            if soldier_change[x][y] > 0:
                soldier[x][y] = soldier_change[x][y] - soldier[x][y]
            elif soldier_change[x][y] < 0:
                soldier[x][y] += soldier_change[x][y]


def support(country):
    soldier_change = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if area[x][y] == country:
                is_other_country = False
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if area[nx][ny] and area[nx][ny] != country:
                            is_other_country = True
                            break
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if area[nx][ny] == country:
                            if is_other_country and soldier[x][y] <= soldier[nx][ny] * 5:
                                continue
                            soldier_change[x][y] -= (soldier[x][y] // 5)
                            soldier_change[nx][ny] += (soldier[x][y] // 5)
    for x in range(n):
        for y in range(n):
            soldier[x][y] += soldier_change[x][y]


def supply():
    for i in range(n):
        for j in range(n):
            soldier[i][j] += supplement[i][j]


def is_over():
    is_found = False
    for i in range(n):
        for j in range(n):
            if not area[i][j]:
                continue
            if not is_found:
                country = area[i][j]
                is_found = True
                continue
            if country != area[i][j]:
                return False
    return True


def is_country(country):
    for i in range(n):
        for j in range(n):
            if area[i][j] == country:
                return True
    return False


for t in range(1, int(input())+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    soldier = [list(map(int, input().split())) for _ in range(n)]
    supplement = [list(map(int, input().split())) for _ in range(n)]
    
    country = 1
    while not is_over():
        if is_country(country):
            attack(country)
            support(country)
            supply()
        country += 1
        if country > 3:
            country = 1

    total = 0
    for line in soldier:
        total += sum(line)
    print('#%s %s' % (t, total))