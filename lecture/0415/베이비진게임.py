CARD_RANGE = 10
CARD_COUNT = 12
TRIPLET = 3
RUN_MIN_INDEX = 7
MIN_CARDS_FOR_BABYGIN = 4
DRAW, FIRST, SECOND = 0, 1, 2


def is_babygin(player):
    for i in range(CARD_RANGE):
        if player[i] >= TRIPLET:
            return True
        if i <= RUN_MIN_INDEX and all([player[i], player[i+1], player[i+2]]):
            return True
    return False


for t in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    first, second = [0]*CARD_RANGE, [0]*CARD_RANGE
    winner = DRAW
    for i in range(0, CARD_COUNT, 2):
        first[cards[i]] += 1
        second[cards[i+1]] += 1
        if i >= MIN_CARDS_FOR_BABYGIN:
            if is_babygin(first):
                winner = FIRST
                break
            if is_babygin(second):
                winner = SECOND
                break
    print('#%s %s' % (t, winner))