# 14502. 연구소 (골드5)

import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and lab[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
virus, space = [], []
max_safety_zone = 0

# 바이러스와 빈 공간 위치 목록 만들기
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            space.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

for wall1, wall2, wall3 in combinations(space, 3):
    # 벽 3개 추가로 세우기
    lab[wall1[0]][wall1[1]] = 1
    lab[wall2[0]][wall2[1]] = 1
    lab[wall3[0]][wall3[1]] = 1

    # 바이러스 퍼뜨리기(bfs)
    visited = [[False] * m for _ in range(n)]
    bfs(deque(virus))

    # 안전영역 개수 세기
    safety_zone = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0 and not visited[i][j]:
                safety_zone += 1

    # 안전 영역 최대 크기 비교
    max_safety_zone = max(max_safety_zone, safety_zone)

    # 벽 3개 다시 허물기
    lab[wall1[0]][wall1[1]] = 0
    lab[wall2[0]][wall2[1]] = 0
    lab[wall3[0]][wall3[1]] = 0

print(max_safety_zone)
