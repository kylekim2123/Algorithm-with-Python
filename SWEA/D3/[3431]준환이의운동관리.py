# 3431. 준환이의 운동 관리

for t in range(1, int(input())+1):
    l, u, x = map(int, input().split())
    if x > u:
        result = -1
    elif x >= l:
        result = 0
    else:
        result = l - x
    print(f'#{t} {result}')