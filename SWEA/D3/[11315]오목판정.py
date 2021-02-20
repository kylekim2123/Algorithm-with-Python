# 11315. 오목 판정

def is_five(board, n):
    dr = [1, 1, 1, 0] # 좌하, 하, 우하, 우
    dc = [-1, 0, 1, 1]
    for r in range(n):
        for c in range(n):
            for i in range(4):
                temp_r, temp_c = r, c
                for _ in range(5):
                    if temp_r < 0 or temp_r >= n or temp_c < 0 or temp_c >= n or board[temp_r][temp_c] != 'o':
                        break
                    temp_r += dr[i]
                    temp_c += dc[i]
                else:
                    return True
    return False

for t in range(1, int(input())+1):
    n = int(input())
    board = [input() for _ in range(n)]
    result = 'YES' if is_five(board, n) else 'NO'
    print(f'#{t} {result}')