# 1225. S/W 문제해결 기본 7일차 - 암호생성기

for _ in range(1, 11):
    t = int(input())
    numbers = list(map(int, input().split()))
    minus = 1
    while(True):
        numbers.append(numbers.pop(0) - minus)
        if numbers[-1] <= 0:
            numbers[-1] = 0
            break
        minus = 1 if minus == 5 else minus + 1
    print(f'#{t}', end=' ')
    print(*numbers)