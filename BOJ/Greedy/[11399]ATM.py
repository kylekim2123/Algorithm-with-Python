# 11399. ATM (실버3)

n = int(input())
minutes = sorted(map(int, input().split()))
total = 0

for i in range(n):
    total += sum(minutes[: i + 1])

print(total)
