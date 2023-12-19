# 배터리 소비량 구하는 함수
def calculate_battery(routes):
    return sum(battery[routes[i]][routes[i+1]] for i in range(len(routes)-1))


# 가능한 경로를 찾는 함수 (순열 탐색)
def find_possible_route(idx, check, perm):
    if idx == pick_count: # 순열이 완성 되면
        global min_total
        min_total = min(min_total, calculate_battery([0] + perm + [0])) # 최소 소비량 갱신
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
    pick_count = len(areas) # 몇 개를 뽑아서 순열을 만들 것인지
    min_total = 10 * 10 * 100 # 문제의 조건에서 가능한 최대값으로 초기화
    find_possible_route(0, 0, [0] * pick_count)
    print('#%s %s' % (t, min_total))
    