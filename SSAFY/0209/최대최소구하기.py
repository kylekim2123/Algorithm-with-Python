def get_maximum(args):
    max_num = args[0]
    for arg in args:
        if arg > max_num:
            max_num = arg
    return max_num


def get_minimum(args):
    min_num = args[0]
    for arg in args:
        if arg < min_num:
            min_num = arg
    return min_num


T = int(input())
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    result = get_maximum(numbers) - get_minimum(numbers)
    print('#%s %s' % (t, result))