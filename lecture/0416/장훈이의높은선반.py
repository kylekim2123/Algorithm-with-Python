from itertools import combinations

for t in range(1, int(input())+1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    min_height = 20 * 10000
    is_find_min = False
    for i in range(n, 0, -1):
        for case in combinations(heights, i):
            tower = sum(case)
            if b <= tower < min_height:
                min_height = tower
            if b == tower:
                is_find_min = True
                break
        if is_find_min:
            break
    print('#%s %s' % (t, min_height-b))