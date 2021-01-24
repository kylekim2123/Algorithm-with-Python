# 1970. 쉬운 거스름돈

for t in range(1, int(input()) + 1):
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    need = [0, 0, 0, 0, 0, 0, 0, 0]
    n = int(input())
    for i in range(8):
        if n // moneys[i] != 0:
            need[i] += (n // moneys[i])
            n %= moneys[i]
    print(f'#{t}')
    print(*need)