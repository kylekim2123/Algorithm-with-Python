def turn(n, arr):
    # j는 row, i는 column이다. row는 역방향, column은 정방향으로 읽어 배열을 90도 회전한다.
    new_arr = [''.join([arr[j][i] for j in range(n-1, -1, -1)]) for i in range(n)]
    return new_arr


for t in range(1, int(input()) + 1):
    n = int(input())
    turn1 = turn(n, [input().split() for _ in range(n)])
    turn2 = turn(n, turn1)
    turn3 = turn(n, turn2)

    print('#%s' % t)
    for i in range(n):
        print(' '.join([turn1[i], turn2[i], turn3[i]]))
