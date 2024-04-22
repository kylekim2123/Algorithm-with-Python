# 브론즈 1

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    ta, tb, va, vb = map(int, input().split())
    total_a, total_b = ta * va, tb * vb

    if total_a <= total_b:
        print(total_b)
        continue

    remaining_tasks = (total_a - total_b) // ta
    remaining_time = (total_a - total_b) % ta
    result = total_b

    if remaining_tasks % 2 == 0:
        result += ((remaining_tasks // 2) * ta) + remaining_time
    else:
        result += (remaining_tasks // 2 + 1) * ta

    print(result)
