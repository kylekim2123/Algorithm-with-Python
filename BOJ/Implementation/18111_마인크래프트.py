# 실버 2

import sys

input = sys.stdin.readline


def flatten(inventory, seconds):
    for i in range(n):
        for j in range(m):
            if land[i][j] > height:
                inventory += land[i][j] - height
                seconds += (land[i][j] - height) * 2
            elif land[i][j] < height:
                inventory -= height - land[i][j]
                seconds += height - land[i][j]

            if seconds >= result_seconds:
                return -1, -1

    return inventory, seconds


n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
result_height, result_seconds = 0, 99999999

for height in range(max(map(max, land)), min(map(min, land)) - 1, -1):
    left_inventory, seconds = flatten(b, 0)

    if left_inventory < 0:
        continue

    if seconds < result_seconds:
        result_seconds = seconds
        result_height = height

print(result_seconds, result_height)
