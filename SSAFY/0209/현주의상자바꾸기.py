T = int(input())
for t in range(1, T+1):
    n, q = map(int, input().split())
    box = [0] * n
    for i in range(1, q+1):
        left, right = map(int, input().split())
        for j in range(left-1, right):
            box[j] = i
    print('#%s' % t, end=' ')
    print(*box)
