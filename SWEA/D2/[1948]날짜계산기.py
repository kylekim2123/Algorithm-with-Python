# 1948. 날짜 계산기

def find_days(month):
    if month == 2:
        return 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return 30

for t in range(1, int(input()) + 1):
    date = list(map(int, input().split()))
    if date[0] == date[2]: # 월이 같으면 일수로만 계산
        print(f'#{t} {date[3] - date[1] + 1}')
    else:
        total = find_days(date[0]) - date[1] + 1
        for i in range(date[0] + 1, date[2]):
            total += find_days(i)
        total += date[3]
        print(f'#{t} {total}')