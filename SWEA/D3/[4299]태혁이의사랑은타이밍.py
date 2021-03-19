# 4299. 태혁이의 사랑은 타이밍

for t in range(1, int(input())+1):
    d, h, m = map(int, input().split())
    print(f'#{t}', end=' ')
    if d == 11 and (h < 11 or (h == 11 and m < 11)):
        print(-1)
        continue
    if d == 11:
        print((h-11)*60 + (m-11))
        continue
    print(((d-11)*24+(h-11))*60 + (m-11))
