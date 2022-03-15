# 11047. 동전0 (실버3)

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
total = 0

for i in range(n - 1, -1, -1):
    total += k // A[i]
    k %= A[i]

print(total)
