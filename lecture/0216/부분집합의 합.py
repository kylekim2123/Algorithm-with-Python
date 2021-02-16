def get_sum(args):
    total = 0
    for arg in args:
        total += arg
    return total


A = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
SIZE = 12
T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    count = 0
    for i in range(1, 1 << SIZE):
        subset = []
        for j in range(SIZE):
            if i & (1 << j):
                subset.append(A[j])
        if len(subset) == n and get_sum(subset) == k:
            count += 1
    print('#%s %s' % (t, count))
