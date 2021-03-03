for _ in range(1, 11):
    t = input()
    queue = list(map(int, input().split()))
    turn = 1
    while True:
        queue.append(queue.pop(0) - turn)
        if queue[-1] <= 0:
            queue[-1] = 0
            break
        turn = 1 if turn == 5 else turn + 1
    print('#%s' % t, *queue)
