for t in range(1, int(input())+1):
    cnt = [0] * 10
    for card in map(int, input()[:6]):
        cnt[card] += 1
    
    i, babygin = 0, 0
    result = 'Lose'
    while i <= 9:
        if babygin == 2:
            result = 'Baby Gin'
            break
        if cnt[i] >= 3:
            babygin += 1
            cnt[i] -= 3
            continue
        if i <= 7 and all((cnt[i], cnt[i+1], cnt[i+2])):
            babygin += 1
            for j in range(3):
                cnt[i+j] -= 1
            continue
        i += 1
        
    print('#%s %s' % (t, result))
