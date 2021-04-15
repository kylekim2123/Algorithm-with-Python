for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    wi = sorted(map(int, input().split()))
    tj = sorted(map(int, input().split()))
    i, j, total_weight = n-1, m-1, 0
    while i >= 0 and j >= 0:
        if wi[i] <= tj[j]:
            total_weight += wi[i]
            j -= 1
        i -= 1
    print('#%s %s' % (t, total_weight))