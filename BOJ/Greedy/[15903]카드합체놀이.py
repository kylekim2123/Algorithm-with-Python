# 15903. 카드 합체 놀이(실버3)

n, m = map(int, input().split())
card = list(map(int, input().split()))
for _ in range(m):
    card.sort()
    sum_mins = card[0] + card[1]
    card[0], card[1] = sum_mins, sum_mins
print(sum(card))