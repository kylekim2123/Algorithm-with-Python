CARD_RANGE = 10 # 카드 숫자의 범위(0~9)
CARD_COUNT = 12 # 1게임당 플레이어에게 나눠주는 총 카드 수 12장
TRIPLET = 3 # triplet이 되기 위한 조건
RUN_MAX_INDEX = 7 # run을 확인하기 위한 인덱스의 마지노선
MIN_CARDS_FOR_BABYGIN = 4 # 4장 넘게 뿌리기 전에는, 각 플레이어가 2장 이하씩 카드를 가지고 있으므로, babygin이 성립될 수 없다.
DRAW, FIRST, SECOND = 0, 1, 2 # 무승부, 플레이어1우승, 플레이어2우승


# 플레이어가 babygin인지 확인하는 함수
def is_babygin(player):
    for i in range(CARD_RANGE):
        if player[i] >= TRIPLET:
            return True # triplet
        if i <= RUN_MAX_INDEX and all([player[i], player[i+1], player[i+2]]):
            return True # run
    return False # babygin 아님


for t in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    first, second = [0]*CARD_RANGE, [0]*CARD_RANGE # 플레이어1과 플레이어2가 보유한 카드 종류를 담는 배열
    winner = DRAW # 승자는 무승부로 초기화
    for i in range(0, CARD_COUNT, 2): # 2씩 뛰어넘는 이유는, 한번에 두 명의 플레이어에게 한 장씩, 즉 2장을 나눠주기 때문
        first[cards[i]] += 1 # 플레이어1 카드 받음
        second[cards[i+1]] += 1 # 플레이어2 카드 받음
        if i >= MIN_CARDS_FOR_BABYGIN: # babygin이 만들어지기 위한 최소 조건을 만족하면 (패에 카드가 3장 이상)
            if is_babygin(first): # 플레이어1이 babygin이라면
                winner = FIRST # 승자는 플레이어1
                break
            if is_babygin(second): # 플레이어2가 babygin이라면
                winner = SECOND # 승자는 플레이어2
                break
    print('#%s %s' % (t, winner))