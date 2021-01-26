# 1986. 지그재그 숫자

for t in range(1, int(input()) + 1):
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total -= i
        else:
            total += i
    print(f'#{t} {total}')