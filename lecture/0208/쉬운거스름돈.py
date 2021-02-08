T = int(input())
for t in range(1, T+1):
    money = int(input())
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10] # 돈의 단위
    unit_count = [0] * 8 # 각 단위가 필요한 횟수 저장

    for i in range(8):
        unit_count[i] = money // units[i]
        money %= units[i]

    print('#%s' % t)
    print(*unit_count)