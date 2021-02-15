# 2563. 색종이 (실버5)

n = int(input())
paper = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

total = 0
for line in paper:
    total += sum(line)

print(total)