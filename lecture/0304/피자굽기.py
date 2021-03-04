for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    queue = [i for i in range(n)] # 화로에 넣는 치즈들의 인덱스를 담는다.
    temp = n # 화로 안에 있는 치즈가 녹았을 때, 교체할 다음 치즈의 인덱스
    while len(queue) > 1:
        i = queue.pop(0) # 1번 위치의 치즈를 꺼낸다.
        cheese[i] //= 2 # 녹는다.
        if cheese[i] > 0: # 아직 다 안녹았으면
            queue.append(i) # 다시 넣는다.
        elif temp < m: # 다 녹았는데, 다음 치즈가 있으면
            queue.append(temp) # 다음 치즈를 넣는다.
            temp += 1 # 다음 치즈의 인덱스를 갱신한다.
    print('#%s %s' % (t, queue[0]+1))
