# 2847. 게임을 만든 동준이(실버4)

n = int(input())
scores = [int(input()) for _ in range(n)]
count = 0
for i in range(n-2, -1, -1):
    if scores[i] >= scores[i+1]:
        decreasing = scores[i] - scores[i+1] + 1
        count += decreasing
        scores[i] -= decreasing
print(count)