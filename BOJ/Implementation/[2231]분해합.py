# 2231. 분해합 (브론즈2)

n = int(input())
start = n - (len(str(n)) * 9)
if start < 0:
    start = 1
for i in range(start, n):
    total = i + sum(map(int, str(i)))
    if total == n:
        print(i)
        break
else:
    print(0)
