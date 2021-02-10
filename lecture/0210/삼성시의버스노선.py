T = int(input())
for t in range(1, T+1):
    n = int(input())
    bus_lines = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    bus_stops = [int(input()) for _ in range(p)]
    result = [0] * p

    for bus_line in bus_lines:
        for i in range(p):
            if bus_line[0] <= bus_stops[i] <= bus_line[1]:
                result[i] += 1
    print('#%s' % t, end=' ')
    print(*result)
