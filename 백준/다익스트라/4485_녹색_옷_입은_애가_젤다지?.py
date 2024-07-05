# 골드 4

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
DX, DY = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상, 하, 좌, 우
INF = 9999999


def dijkstra(x, y):
    distance[x][y] = maze[x][y]  # 시작 좌표에 대한 비용 초기화
    heap = [(maze[x][y], x, y)]  # (비용, x좌표, y좌표)

    while heap:
        min_dist, x, y = heappop(heap)  # 최소 비용으로 갈 수 있는 좌표 정보를 힙에서 꺼내기

        if distance[x][y] < min_dist:
            continue  # 이미 기록된 최소 비용보다 크면 탐색할 필요가 없음

        for i in range(4):  # 상하좌우 인접한 곳으로 이동하며
            nx, ny = x + DX[i], y + DY[i]

            if 0 <= nx < n and 0 <= ny < n:  # 좌표 범위 내에 있다면
                next_dist = min_dist + maze[nx][ny]  # 다음 좌표까지 가는 비용 계산

                if next_dist < distance[nx][ny]:  # 만약 이미 기록된 최소 비용보다 새로운 비용이 작으면
                    distance[nx][ny] = next_dist  # 최소 비용 갱신
                    heappush(heap, (next_dist, nx, ny))  # 다음 탐색을 위해 힙에 삽입


t = 1

while True:
    n = int(input())

    if n == 0:
        break  # n이 0이 주어지면 전체 입력 종료

    maze = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    dijkstra(0, 0)

    print(f"Problem {t}: {distance[-1][-1]}")

    t += 1
