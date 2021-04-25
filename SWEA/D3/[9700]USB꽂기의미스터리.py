# 9700. USB 꽂기의 미스터리

for t in range(1, int(input())+1):
    p, q = map(float, input().split())
    print(f'#{t} YES') if (1-p)*q < p*(1-q)*q else print(f'#{t} NO')
