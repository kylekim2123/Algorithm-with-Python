# 7560. ATM

n = int(input())
p = sorted(map(int, input().split()))
result = [p[0]]
for i in range(1, n):
    result.append(result[-1] + p[i])
print(sum(result))