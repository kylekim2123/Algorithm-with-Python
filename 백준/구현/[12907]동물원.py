# 12907. 동물원 (골드5)

n = input()
answer = sorted(map(int, input().split()))

if answer[0] > 0:
    print(0)
else:
    cat, rabbit, count = 0, 0, 1
    for ans in answer:
        if ans == cat and ans == rabbit:
            cat += 1
            count += count
        elif ans == cat:
            cat += 1
        elif ans == rabbit:
            rabbit += 1
        else:
            count = 0
            break
    print(count)