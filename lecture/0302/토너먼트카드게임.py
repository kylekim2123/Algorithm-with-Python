# 가위바위보 승자 판별
def get_winner(p1, p2):
    battle = abs(cards[p1]-cards[p2])
    if battle == 1: # (가위 vs 바위) 또는 (바위 vs 보)
        return p1 if cards[p1] > cards[p2] else p2
    if battle == 2: # 가위 vs 보
        return p1 if cards[p1] < cards[p2] else p2
    return min(p1, p2) # 비기는 경우

def play(start, end):
    if start == end:
        return start # 원소가 하나면 반환
    center = (start+end) // 2
    return get_winner(play(start, center), play(center+1, end)) # 분할정복

for t in range(1, int(input())+1):
    n = int(input())
    cards = list(map(int, input().split()))
    print('#%s %s' % (t, play(0, n-1)+1)) # 1번 선수부터 있으므로 마지막에 + 1
