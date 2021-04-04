# 5515. 2016년 요일 맞추기

def get_days(month):
    days = 0
    for i in range(1, month):
        if i in {1, 3, 5, 7, 8, 10, 12}:
            days += 31
        elif i in {4, 6, 9, 11}:
            days += 30
        else:
            days += 29
    return days

for t in range(1, int(input())+1):
    m, d = map(int, input().split())
    result = (((get_days(m) + d - 1) % 7) + 4) % 7
    print(f'#{t} {result}')