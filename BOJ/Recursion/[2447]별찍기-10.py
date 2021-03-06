# 2447. 별 찍기-10 (실버1)

def star(row, col, number):
    if number == 1: # base case
        board[row][col] = '*'
        return
    number //= 3 # 구간을 쪼개기 위함
    # i, j가 9분할 하는 각각의 영역을 의미
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: # 가운데 영역은 빈칸으로 냅둔다
                continue
            star(row+(i*number), col+(j*number), number) # 재귀로 들어가더라도, board의 원래 좌표는 찾아야 하므로 row와 col에 각각 더한다.
    
n = int(input())
board = [[' '] * n for _ in range(n)]
star(0, 0, n)
print('\n'.join(''.join(line) for line in board))
