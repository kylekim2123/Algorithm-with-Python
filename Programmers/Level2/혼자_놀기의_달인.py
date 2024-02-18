# Level 2

def solution(cards):
    cards = [0] + cards
    visited = [False] * (len(cards) + 1)
    groups = []

    for card in cards:
        if visited[card]:
            continue

        group = []
        temp = card

        while not visited[temp]:
            visited[temp] = True
            group.append(temp)
            temp = cards[temp]

        groups.append(group)

    result = sorted(groups[1:], key=lambda x: len(x), reverse=True)

    return len(result[0]) * len(result[1]) if len(result) > 1 else 0
