# 15683. 감시 (골드4)

import sys
import copy

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cctv_dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    5: [[0, 1, 2, 3]],
}


def monitor(cctv_info):
    visited = [[False] * m for _ in range(n)]
    for direction, x, y in cctv_info:
        for i in direction:
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < n and 0 <= ny < m and room[nx][ny] != 6:
                visited[nx][ny] = True
                nx += dx[i]
                ny += dy[i]
    return visited


def set_min_invisible(visited):
    global min_invisible
    total = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and room[i][j] == 0:
                total += 1
    min_invisible = min(min_invisible, total)


def get_cctv_info(depth, cctv_info):
    if depth == len(cctv):
        visited = monitor(cctv_info)
        set_min_invisible(visited)
        return
    cctv_num, x, y = cctv[depth]
    for direction in cctv_dirs[cctv_num]:
        cctv_info.append((direction, x, y))
        get_cctv_info(depth + 1, copy.deepcopy(cctv_info))
        cctv_info.pop()


n, m = map(int, input().split())
room, cctv = [], []
min_invisible = n * m
for i in range(n):
    line = list(map(int, input().split()))
    room.append(line)
    for j in range(m):
        if line[j] in cctv_dirs:
            cctv.append((line[j], i, j))

get_cctv_info(0, [])
print(min_invisible)
