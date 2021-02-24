for t in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    seconds = list(map(int, input().split()))
    length = (11111//m) + 1
    clients = [0] * length
    for second in seconds:
        clients[second//m] += 1
    if clients[0] > 0:
        print('#%s Impossible' % t)
        continue
    fish = 0
    for i in range(1, length):
        fish += (k - clients[i])
        if fish < 0:
            print('#%s Impossible' % t)
            break
    else:
        print('#%s Possible' % t)
