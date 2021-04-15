for t in range(1, int(input())+1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]
    time.sort(key=lambda x: x[1])
    max_truck, previous_end = 0, 0
    for s, e in time:
        if s >= previous_end:
            max_truck += 1
            previous_end = e
    print('#%s %s' % (t, max_truck))