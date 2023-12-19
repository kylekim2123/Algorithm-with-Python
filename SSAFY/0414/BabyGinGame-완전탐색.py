# 풀이1. 모든 순열 완전탐색
CARD_COUNT = 6

def is_run(half_cards):
    for i in range(len(half_cards)-1):
        if half_cards[i] + 1 != half_cards[i+1]:
            return False
    return True


def is_triplet(half_cards):
    for i in range(len(half_cards)-1):
        if half_cards[i] != half_cards[i+1]:
            return False
    return True


def is_each_case_baby_gin(left, right):
    four_conditions = [
        is_run(left) and is_run(right),
        is_run(left) and is_triplet(right),
        is_triplet(left) and is_run(right),
        is_triplet(left) and is_triplet(right)
    ]
    return any(four_conditions)


def is_baby_gin(case):
    half = CARD_COUNT // 2
    if is_each_case_baby_gin(case[:half], case[half:]):
        return 'Baby Gin'
    return 'Lose'


def get_permutation(idx, check, card):
    global result
    if result == 'Baby Gin':
        return
    if idx == CARD_COUNT:
        result = is_baby_gin(card)
        return
    for i in range(CARD_COUNT):
        if check & (1 << i):
            continue
        card[idx] = cards[i]
        get_permutation(idx + 1, check | (1 << i), card)


for t in range(1, int(input())+1):
    cards = list(map(int, input()[:CARD_COUNT]))
    result = 'Lose'
    get_permutation(0, 0, [0] * CARD_COUNT)
    print('#%s %s' % (t, result))
