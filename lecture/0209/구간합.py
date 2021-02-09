def get_sum(args):
    total = 0
    for arg in args:
        total += arg
    return total


T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    maximum = get_sum(numbers[:m])
    minimum = maximum
    for i in range(1, n-m+1):
        this_sum = get_sum(numbers[i:i+m])
        if this_sum > maximum:
            maximum = this_sum
        elif this_sum < minimum:
            minimum = this_sum
    print('#%s %s' % (t, maximum-minimum))
