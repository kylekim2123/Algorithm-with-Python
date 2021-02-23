for t in range(1, int(input())+1):
    n = int(input())
    prices = list(map(int, input().split()))
    benefit, max_price = 0, prices[-1]
    for i in range(n-2, -1, -1):
        if prices[i] >= max_price:
            max_price = prices[i]
            continue
        benefit += (max_price - prices[i])
    print('#%s %s' % (t, benefit))