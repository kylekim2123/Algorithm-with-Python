# 1860. 진기의 최고급 붕어빵
for t in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    seconds = list(map(int, input().split()))
    clients = [0] * 11112

    for second in seconds:
        clients[second//m] += 1
    
    if clients[0] != 0:
        print(f'#{t} Impossible')
    else:
        temp = 0
        for i in range(1, 11112):
            temp += k - clients[i]
            if temp < 0:
                print(f'#{t} Impossible')
                break
        else:
            print(f'#{t} Possible')
    

    
        