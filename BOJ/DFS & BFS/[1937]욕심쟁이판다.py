# 1937. 욕심쟁이 판다 (골드3)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if not memo[x][y]: # 메모에 없다면 메모를 하고 반환한다.
        memo[x][y] = 1 # 기본적으로 판다는 하루를 살 수 있음
        k = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and forest[x][y] < forest[nx][ny]:
                k = max(k, dfs(nx, ny)) # 사방에서 탐색한 k 중 가장 큰 k 찾기
        memo[x][y] += k # k 만큼 더하면 해당 좌표에서 살 수 있는 일 수가 확정
    return memo[x][y] # 메모가 있다면 바로 메모를 반환, 없다면 k를 찾아 더해서 반환

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
memo = [[0]*n for _ in range(n)] # Dynamic Programming Memoization
max_k = 0
for i in range(n):
    for j in range(n):
        max_k = max(max_k, dfs(i, j))
print(max_k)