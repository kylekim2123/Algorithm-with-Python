# 1284. 수도 요금 경쟁

results = list()
for t in range(1, int(input()) + 1):
    pqrsw = list(map(int, input().split()))
    p = pqrsw[0]  # A사의 1리터 당 가격
    q = pqrsw[1]  # B사의 기본요금
    r = pqrsw[2]  # B사의 월간 사용량 기준
    s = pqrsw[3]  # B사의 초과량에 대한 1리터 당 가격
    w = pqrsw[4]  # 종민이의 월간 사용량

    cost_A = p * w
    cost_B = q
    if w > r:
        cost_B += (w - r) * s
    results.append(f'#{t} {min(cost_A, cost_B)}')

for result in results:
    print(result)
