# 1859. 백만 장자 프로젝트

for t in range(1, int(input()) + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    benefit = 0
    max_price = prices.pop()
    while prices:
        now_price = prices.pop()
        if now_price >= max_price:
            max_price = now_price
            continue
        benefit += max_price - now_price
    print(f'#{t} {benefit}')
