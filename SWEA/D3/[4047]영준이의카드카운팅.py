# 4047. 영준이의 카드 카운팅

for t in range(1, int(input())+1):
    cards = input()
    pattern = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    existed = []
    for i in range(0, len(cards)-2, 3):
        card = cards[i:i+3]
        if card in existed:
            print(f'#{t} ERROR')
            break
        existed.append(card)
        pattern[card[0]] -= 1
    else:
        result = ' '.join(map(str, pattern.values()))
        print(f'#{t} {result}')