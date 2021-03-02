# 2573. 빙산 (골드4)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빙하가 모두 녹았는지 확인하는 함수
def is_all_melted():
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ocean[i][j]:
                return False
    return True

# 주변의 접한 바다만큼 빙하를 녹이는 함수
def melt():
    for i in range(1, n-1):
        for j in range(1, m-1):
            if melting_count[i][j] > 0:
                ocean[i][j] -= melting_count[i][j]
                if ocean[i][j] < 0:
                    ocean[i][j] = 0 # 빙하는 음수일 수 없음

# 빙하가 한 덩어리인지 확인하는 함수
def is_one_mass():
    did_dfs = False # dfs를 두번 들어가는지 확인
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ocean[i][j] != 0:
                for k in range(4):
                    if ocean[i+dx[k]][j+dy[k]] == 0:
                        melting_count[i][j] += 1 # 주변의 바다만큼 얼마나 빙하를 녹이는지 구함
                if not visited[i][j]:
                    if did_dfs:
                        return False # 이미 dfs를 한번 했었는데, 다시 진입하면 덩어리가 2개 이상이라는 것임
                    visited[i][j] = True
                    did_dfs = True
                    dfs(i, j)
    return True

def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ocean[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)

n, m = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(n)]
time = 0
while not is_all_melted(): # 다 녹지 않는 동안
    visited = [[False] * m for _ in range(n)]
    melting_count = [[0] * m for _ in range(n)]
    if not is_one_mass(): # 빙하가 두 덩어리 이상이면
        print(time) # 최소 년도 출력하고 break
        break
    time += 1
    melt() # 빙하 녹이기
else:
    print(0) # 빙하가 다 녹아도 분리되지 않으면 0 출력
