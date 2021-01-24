# 1959. 두 개의 숫자열

def max_numbers(short_list, long_list):
    for i in range(len(long_list) - len(short_list) + 1):
        fixed_long = long_list[i:i + len(short_list)]
        total = 0
        for j in range(len(short_list)):
            total += short_list[j] * fixed_long[j]
        if (i == 0) or (max_num < total):
            max_num = total
    return max_num

for t in range(1, int(input()) + 1):
    nm = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    print(f'#{t}', end=' ')
    if len(ai) > len(bj):
        print(max_numbers(bj, ai))
    else:
        print(max_numbers(ai, bj))
    