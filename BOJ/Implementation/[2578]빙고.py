# 2578. 빙고 (실버5)
import sys

def get_bingo():
    bingo = 0
    for i in range(5):
        for j in range(5):
            if bingo_map[i][j] != '0':
                break
        else:
            bingo += 1

        for j in range(5):
            if bingo_map[j][i] != '0':
                break
        else:
            bingo += 1

    for i in range(5):
        if bingo_map[i][i] != '0':
            break
    else:
        bingo += 1

    for i in range(4, -1, -1):
        if bingo_map[i][5-i-1] != '0':
            break
    else:
        bingo += 1
    
    return bingo

bingo_map = [list(input().split()) for _ in range(5)]
numbers = [list(input().split()) for _ in range(5)]
count = 0
for line in numbers:
    for number in line:
        count += 1
        for i in range(5):
            for j in range(5):
                if number == bingo_map[i][j]:
                    bingo_map[i][j] = '0'
                    if get_bingo() >= 3:
                        print(count)
                        sys.exit()
