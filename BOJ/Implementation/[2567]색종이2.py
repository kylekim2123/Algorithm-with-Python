# 2567. 색종이 2 (실버5)

n = int(input())
size = 101
paper = [[0] * size for _ in range(size)]
dx = (-1, 1, 0, 0) # 상 하 좌 우
dy = (0, 0, -1, 1)
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 2

total = 0
for i in range(1, size):
    for j in range(1, size):
        if paper[i][j] == 2:
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if (0 <= ni < size) and (0 <= nj < size):
                    if paper[ni][nj] == 0:
                        total += 1
print(total)
