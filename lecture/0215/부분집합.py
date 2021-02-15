n = 10
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    for i in range(1, 1 << n):
        subset_sum = 0
        for j in range(n):
            if i & (1 << j):
                subset_sum += numbers[j]
        if subset_sum == 0:
            print('#%s 1' % t)
            break
    else:
        print('#%s 0' % t)
