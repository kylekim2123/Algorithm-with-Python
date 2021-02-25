for t in range(1, int(input())+1):
    n, q = map(int, input().split())
    numbers = [0] * n
    for i in range(1, q+1):
        left, right = map(int, input().split())
        for j in range(left-1, right):
            numbers[j] = i
    print('#%s %s' % (t, ' '.join(map(str, numbers))))