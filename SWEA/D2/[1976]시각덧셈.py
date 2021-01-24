# 1976. 시각 덧셈

for t in range(1, int(input()) + 1):
    time = list(map(int, input().split()))
    start_hour = time[0]
    start_minute = time[1]
    end_hour = time[2]
    end_minute = time[3]

    sum_hour = start_hour + end_hour
    sum_minute = start_minute + end_minute

    if sum_minute >= 60:
        sum_hour += 1
        sum_minute -= 60
    if sum_hour > 12:
        sum_hour -= 12

    print(f'#{t} {sum_hour} {sum_minute}')