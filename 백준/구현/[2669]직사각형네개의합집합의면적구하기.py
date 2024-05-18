# 2669. 직사각형 네개의 합집합의 면적 구하기 (브론즈2)

import sys
input = sys.stdin.readline

paper = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

print(sum(sum(line) for line in paper))