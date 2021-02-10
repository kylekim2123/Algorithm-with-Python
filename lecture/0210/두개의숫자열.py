def max_numbers(short_list, long_list, s_length, l_length):
    for i in range(l_length - s_length + 1): # index out of range 방지
        sliced_long = long_list[i:i+s_length]
        total = 0
        for j in range(s_length):
            total += short_list[j] * sliced_long[j]
        if (i == 0) or (max_num < total):
            max_num = total
    return max_num


T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    print('#%s' % t, end=' ')
    if n > m:
        print(max_numbers(bj, ai, m, n))
    else:
        print(max_numbers(ai, bj, n, m))