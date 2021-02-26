# 3456. 직사각형 길이 찾기

for t in range(1, int(input())+1):
    a, b, c = map(int, input().split())
    if a == b == c:
        print(f'#{t} {a}')
    elif a == b:
        print(f'#{t} {c}')
    elif b == c:
        print(f'#{t} {a}')
    elif a == c:
        print(f'#{t} {b}')