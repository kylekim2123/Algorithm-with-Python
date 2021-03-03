for _ in range(1, 11):
    t = input()
    queue = list(map(int, input().split()))
    turn = 1 # 한 사이클 동안 차례로 빼는 숫자
    while True:
        queue.append(queue.pop(0) - turn) # 맨 앞에 있는 숫자를 빼서 맨 뒤에 넣는다.
        if queue[-1] <= 0:
            queue[-1] = 0
            break # 맨 뒤가 0 이하일 때 암호화 종료
        turn = 1 if turn == 5 else turn + 1 # 사이클 하나가 종료되면 빼는 숫자를 1로 초기화
    print('#%s' % t, *queue)
