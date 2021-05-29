# 2210. 숫자판 점프 (실버2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y, number):
    if len(number) >= 6:
        cases.add(number)
        return
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, number+numbers[nx][ny])

numbers = [input().split() for _ in range(5)]
cases = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, numbers[i][j])

print(len(cases))