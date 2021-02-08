def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


def is_baby_gin(pcards):
    bubble_sort(pcards) # 정렬을 통해서 더 간편한 완전 탐색 조건을 만듦
    length = len(pcards) # 길이는 자주 사용하므로 미리 저장

    # 1. 같은 숫자 3개가 있는 경우
    is_same = False
    for i in range(length):
        for j in range(1, length):
            for k in range(2, length):
                if pcards[i] == pcards[j] and pcards[j] == pcards[k]:
                    is_same = True
                    same = [pcards[i], pcards[j], pcards[k]] # 같은 숫자 3개
                    others = []
                    for x in range(length):
                        if x != i and x != j and x != k:
                            others.append(pcards[x]) # 같은 숫자 3개 이외의 나머지 숫자 3개

    # 나머지 숫자도 3개가 다 같거나 연속이면 baby-gin
    if is_same:
        if others[0] == others[1] and others[1] == others[2]:
            return True
        elif others[0]+1 == others[1] and others[1]+1 == others[2]:
            return True

    # 2. 같은 숫자가 3개 없는 경우, baby-gin이 되려면 연속하는 숫자 뭉치가 2 묶음이어야한다.
    for i in range(length):
        for j in range(1, length):
            for k in range(2, length):
                if pcards[i]+1 == pcards[j] and pcards[j]+1 == pcards[k]:
                    serial = [pcards[i], pcards[j], pcards[k]] # 연속되는 숫자 3개
                    others = []
                    for x in range(length):
                        if x != i and x != j and x != k:
                            others.append(pcards[x]) # 연속되는 숫자 3개 이외의 나머지 숫자 3개
                    if others[0]+1 == others[1] and others[1]+1 == others[2]:
                        return True # 나머지 숫자도 연속되면 baby-gin
                    return False

    return False # 어느 것도 해당 안되는 경우


T = int(input())
for t in range(1, T+1):
    cards = list(map(int, input()))
    if is_baby_gin(cards):
        print('#%s Baby Gin' % t)
    else:
        print('#%s Lose' % t)
