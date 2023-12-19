from itertools import combinations


# 비상구 탈출 시간 구하기
def set_second(exit_people, ex, ey):
    length = n + n + 10
    exit_seconds = [0] * length

    # 1. 이동 시간
    for x, y in exit_people:
        distance = abs(x - ex) + abs(y - ey) + 1
        exit_seconds[distance] += 1

    # 2-1. 1초에 한 명만 탈출 가능하므로, 계속 뒤로 밀리는 과정
    for i in range(length - 1):
        if exit_seconds[i] > 1:
            exit_seconds[i + 1] += exit_seconds[i] - 1

    # 2-2. 가장 마지막에 탈출한 사람의 시간 => 탈출 시간
    for i in range(length - 1, 0, -1):
        if exit_seconds[i] > 0:
            global second
            if i > second:
                second = i
            break


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우

for t in range(1, int(input()) + 1):
    n = int(input())
    people, exits = set(), []
    min_second = 99999999

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(n):
            if line[j] == 1:
                people.add((i, j))
            elif line[j] == 2:
                exits.append((i, j))

    e1_x, e1_y = exits[0]  # 비상구1
    e2_x, e2_y = exits[1]  # 비상구2

    for i in range(1, len(people) + 1):
        # 사람들을 두 개로 군집화한 모든 경우의 수를 따짐
        for case in combinations(people, i):
            second = 0
            set_second(set(case), e1_x, e1_y)  # 비상구1
            set_second(people - set(case), e2_x, e2_y)  # 비상구2
            min_second = min(second, min_second)

    print(f"#{t} {min_second}")
