# 2167. 2차원 배열의 합 (브론즈1)

n, m = map(int, input().split())
arr = [[0] * (m+1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))
DP = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] + arr[i][j] - DP[i-1][j-1]

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    total = DP[r2][c2] - DP[r2][c1-1] - DP[r1-1][c2] + DP[r1-1][c1-1]
    print(total)