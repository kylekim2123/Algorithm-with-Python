for t in range(1, int(input())+1):
    check = [0] * 401 # 방문 체크 (방의 번호 만큼 크기 부여: 1 ~ 400)
    for _ in range(int(input())):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start # "5번방 -> 1번방" 일 수 있으므로, 시작이 끝보다 크면 swap
        
        # "3번방 - > 5번방" 이동이나, "4번방 -> 6번방" 이동은 똑같은 동작이다.
        # 왜냐면 전자이든 후자이든, (3, 4, 5, 6)번방의 경로가 겹치기 때문에 복도를 공유하는 것이 똑같다.
        # 따라서 start가 짝수이면 즉 4이면 -1을 해서 3으로 만들고, end가 홀수이면 즉 5이면 +1 해서 6으로 만든 다음
        start -= 0 if start % 2 else 1
        end += 1 if end % 2 else 0
        for i in range(start, end+1):
            check[i] += 1 # 3 ~ 6 까지 모두 check 처리
    print('#%s %s' % (t, max(check))) # 가장 많이 겹친 값이 최단 단위 시간을 의미
