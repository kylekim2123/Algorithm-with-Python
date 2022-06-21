from itertools import combinations


def set_second(exit_people, ex, ey):
    length = n + n + 10
    exit_seconds = [0] * length

    for x, y in exit_people:
        distance = abs(x - ex) + abs(y - ey) + 1
        exit_seconds[distance] += 1

    for i in range(length - 1):
        if exit_seconds[i] > 1:
            exit_seconds[i + 1] += exit_seconds[i] - 1

    for i in range(length - 1, 0, -1):
        if exit_seconds[i] > 0:
            global second
            if i > second:
                second = i
            break


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우

for t in range(1, int(input()) + 1):
    n = int(input())
    factory, people, exits = [], set(), []
    min_second = 99999999

    for i in range(n):
        line = list(map(int, input().split()))
        factory.append(line)
        for j in range(n):
            if line[j] == 1:
                people.add((i, j))
            elif line[j] == 2:
                exits.append((i, j))

    e1_x, e1_y = exits[0]
    e2_x, e2_y = exits[1]

    for i in range(1, len(people) + 1):
        for case in combinations(people, i):
            second = 0
            set_second(set(case), e1_x, e1_y)
            set_second(people - set(case), e2_x, e2_y)
            min_second = min(second, min_second)

    print(f"#{t} {min_second}")
