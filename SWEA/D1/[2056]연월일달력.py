# 2056. 연월일 달력

def validate_month_day(month, day):
    if not 1 <= month <= 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not 1 <= day <= 31:
            return False
    if month in [4, 6, 9, 11]:
        if not 1 <= day <= 30:
            return False
    if month == 2:
        if not 1 <= day <= 28:
            return False
    return True

result = []
for i in range(1, int(input()) + 1):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]
    
    if validate_month_day(int(month), int(day)):
        result.append(f'#{i} {year}/{month}/{day}')
    else:
        result.append(f'#{i} -1')

for i in result:
    print(i)
    
        