for t in range(1, int(input())+1):
    n = int(input())
    total, start = 0, n//2
    for i in range(n):
        line = list(map(int, input()))
        total += sum(line[start:n-start])
        start += 1 if i >= n//2 else -1
    print('#%s %s' % (t, total))
