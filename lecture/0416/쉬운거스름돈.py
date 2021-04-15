MONEY = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, int(input())+1):
    n = int(input())
    needs = []
    for m in MONEY:
        needs.append(n//m)
        n %= m
    print('#%s' % t, ' '.join(map(str, needs)), sep='\n')