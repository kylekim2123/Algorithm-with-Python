def calculate_battery(routes):
    return sum(battery[routes[i]][routes[i+1]] for i in range(len(routes)-1))


def find_possible_route(idx, check, perm):
    if idx == pick_count:
        global min_total
        min_total = min(min_total, calculate_battery([0] + perm + [0]))
        return
    for i in range(pick_count):
        if check & (1 << i):
            continue
        perm[idx] = areas[i]
        find_possible_route(idx + 1, check | (1 << i), perm)


for t in range(1, int(input())+1):
    n = int(input())
    battery = [list(map(int, input().split())) for _ in range(n)]
    areas = list(range(1, n))
    pick_count = len(areas)
    min_total = 10 * 10 * 100
    find_possible_route(0, 0, [0] * pick_count)
    print('#%s %s' % (t, min_total))
    