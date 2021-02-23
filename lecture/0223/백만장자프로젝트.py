for t in range(1, int(input())+1):
    n = int(input())
    prices = list(map(int, input().split())) # 가격 정보
    benefit, max_price = 0, prices[-1] # 이윤, 최대 가격(여기서 최대가격은 가격 중 최대값이 아님, 미래에 팔 때 가장 이윤이 많이 남는 최대 가격을 뜻함)
    for i in range(n-2, -1, -1): # 앞에서 부터 탐색하지 않는 이유는, 앞에서 부터 탐색하면 해당 가격이 최대 가격인지 알 수가 없기 때문.(반복을 많이 해야한다)
        if prices[i] >= max_price: # 뒤에서 부터 앞으로 가면서, 해당 가격이 최대 가격보다 이상이면
            max_price = prices[i] # 최대 가격을 갱신
            continue
        benefit += (max_price - prices[i]) # 해당 가격이 최대 가격보다 미만이면, 이 가격에 사서 최대 가격에 파는 것이 가장 이윤이 많이 남음
    print('#%s %s' % (t, benefit))