for t in range(1, int(input()) + 1):
    n, m, k = map(int, input().split()) # 총 n명의 손님, m초마다 k개의 붕어빵 제작
    seconds = list(map(int, input().split())) # 손님이 오는 초 시간
    length = (11111//m) + 1
    clients = [0] * length
    for second in seconds:
        # 예를 들어 4초에 2개씩 만든다고 할 때, 손님이 0, 1, 2, 3 초에 오면 4로 나눈 나머지가 0이므로 clients[0]에 + 1
        clients[second//m] += 1
    if clients[0] > 0:
        print('#%s Impossible' % t) # 붕어빵을 만들기도 전에 손님이 왔으므로 불가능!
        continue
    fish = 0 # 붕어빵의 수
    for i in range(1, length):
        # 남아있는 붕어빵과 새로 만든 붕어빵으로 손님 수를 충당할 수 있는가?
        fish += (k - clients[i]) # 여기서 fish가 음수가 되면 불가능, 0이상이면 가능!
        if fish < 0:
            print('#%s Impossible' % t)
            break
    else:
        print('#%s Possible' % t)
