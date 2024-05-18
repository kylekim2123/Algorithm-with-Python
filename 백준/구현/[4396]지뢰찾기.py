# 4396. 지뢰 찾기 (실버5)

import sys

input = sys.stdin.readline

n = int(input())
bombs = [input().rstrip() for _ in range(n)]
opens = [input().rstrip() for _ in range(n)]
result = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
is_lose = False

for i in range(n):
    for j in range(n):
        if opens[i][j] == "x":
            if bombs[i][j] == ".":
                for k in range(8):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < n and bombs[ni][nj] == "*":
                        result[i][j] += 1
            else:
                is_lose = True
        else:
            result[i][j] = "."

if is_lose:
    for i in range(n):
        for j in range(n):
            if bombs[i][j] == "*":
                result[i][j] = "*"

print(*["".join(map(str, line)) for line in result], sep="\n")
