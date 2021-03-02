def get_winner(p1, p2):
    battle = abs(cards[p1]-cards[p2])
    if battle == 1:
        return p1 if cards[p1] > cards[p2] else p2
    if battle == 2:
        return p1 if cards[p1] < cards[p2] else p2
    return min(p1, p2)

def play(start, end):
    if start == end:
        return start
    center = (start+end) // 2
    return get_winner(play(start, center), play(center+1, end))

for t in range(1, int(input())+1):
    n = int(input())
    cards = list(map(int, input().split()))
    print('#%s %s' % (t, play(0, n-1)+1))
