T = int(input())
for t in range(1, T+1):
    n = int(input())
    cards = input()

    check = [0] * 10
    for card in cards:
        check[int(card)] += 1

    card_count, card_number = 0, 0
    for i in range(10):
        if check[i] >= card_count:
            card_number, card_count = i, check[i]
    print('#%s %s %s' % (t, card_number, card_count))