def binary_search(target, l, r):
    pre_d = 0
    while l <= r:
        m = (l+r)//2
        if A[m] == target:
            return 1
        if A[m] > target:
            r, d = m-1, -1
        else:
            l, d = m+1, 1
        if pre_d == d:
            break
        pre_d = d
    return 0

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A, B = sorted(map(int, input().split())), list(map(int, input().split()))
    count = 0
    for b in B:
        count += binary_search(b, 0, N-1)
    print('#%s %s' % (t, count))
                