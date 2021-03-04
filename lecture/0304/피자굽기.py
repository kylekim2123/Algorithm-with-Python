for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    queue = [i for i in range(n)]
    temp = n
    while len(queue) > 1:
        i = queue.pop(0)
        cheese[i] //= 2
        if cheese[i] > 0:
            queue.append(i)
        elif temp < m:
            queue.append(temp)
            temp += 1
    print('#%s %s' % (t, queue[0]+1))
