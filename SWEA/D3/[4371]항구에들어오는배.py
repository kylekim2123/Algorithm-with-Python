# 4371. 항구에 들어오는 배

for t in range(1, int(input())+1):
    n = int(input())
    days = [int(input()) for _ in range(n)]
    copy_days = list(days)
    days[0] = 0
    count = 0
    while any(days):
        for i in range(n):
            if days[i]:
                break
        interval = days[i] - 1
        start = days[i]
        for j in range(i, n):
            if copy_days[j] == start:
                days[j] = 0
                start += interval
        count += 1
    print(f'#{t} {count}')