# 1954. 달팽이 숫자

for t in range(1, int(input()) + 1):
    n = int(input())
    turn = 1
    now_number = 1
    snail = [[0 for _ in range(n)] for _ in range(n)]

    row = 0
    column = 0
    count = n
    while now_number <= (n ** 2):
        if turn == 1:
            for i in range(count):
                snail[row][column] = now_number
                now_number += 1
                column += 1
            turn = 2
            row += 1
            column -= 1
            count -= 1
        elif turn == 2:
            for i in range(count):
                snail[row][column] = now_number
                now_number += 1
                row += 1
            turn = 3
            row -= 1
            column -= 1
        elif turn == 3:
            for i in range(count):
                snail[row][column] = now_number
                now_number += 1
                column -= 1
            turn = 4
            row -= 1
            column += 1
            count -= 1
        else:
            for i in range(count):
                snail[row][column] = now_number
                now_number += 1
                row -= 1
            turn = 1
            row += 1
            column += 1
            
    print(f'#{t}')
    for i in snail:
        print(*i)