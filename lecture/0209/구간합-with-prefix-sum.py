T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = [0] * n # numbers 리스트 원소의 누적 합
    sum_list[0] = numbers[0]
    for i in range(1, n):
        sum_list[i] = sum_list[i-1] + numbers[i]

    maximum = sum_list[m-1] # 최대값, 최소값은 첫 구간합으로 초기화
    minimum = maximum
    for i in range(m, n):
        now_sum = sum_list[i] - sum_list[i-m]
        if now_sum > maximum:
            maximum = now_sum
        elif now_sum < minimum:
            minimum = now_sum

    print('#%s %s' % (t, maximum-minimum))