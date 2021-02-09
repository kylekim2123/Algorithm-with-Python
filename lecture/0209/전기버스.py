T = int(input())
for t in range(1, T+1):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split()))
    result = 0
    start = 0
    impossible = False
    while True:
        end = start + k
        if end >= n or impossible:
            break
        for i in range(end, start-1, -1):
            if i == start:
                impossible = True
                break
            if i in stations:
                start = i
                result += 1
                break

    if impossible:
        print('#%s 0' % t)
    else:
        print('#%s %s' % (t, result))