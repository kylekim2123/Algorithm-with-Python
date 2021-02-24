for t in range(1, int(input())+1):
    check = [0] * 401
    for _ in range(int(input())):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        start -= 0 if start % 2 else 1
        end += 1 if end % 2 else 0
        for i in range(start, end+1):
            check[i] += 1
    print('#%s %s' % (t, max(check)))
