# 11387. 몬스터 사냥

for t in range(1, int(input())+1):
    DLN = list(map(int, input().split()))
    d, l, n = DLN[0], DLN[1], DLN[2]
    total_damage = 0
    for i in range(n):
        total_damage += d*(1+(i*(l*0.01)))
    print(f'#{t} {int(total_damage)}')
