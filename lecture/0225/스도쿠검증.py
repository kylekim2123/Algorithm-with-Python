def is_correct(sudoku):
    for line in sudoku:
        if len(set(line)) < 9:
            return False # set으로 변환하면 중복 숫자가 없어지므로, 스도쿠를 검증 할 수 있다.
    return True

def validate(sudoku):
    if not is_correct(sudoku):
        return 0 # 1. 가로 기준 스도쿠 검증하기
    if not is_correct(list(zip(*sudoku))):
        return 0 # 2. 세로 기준 스도쿠 검증하기
    cells = []
    for i in range(0, 6, 3):
        for j in range(0, 7, 3):
            cells.append(sudoku[i][j:j+3] + sudoku[i+1][j:j+3] + sudoku[i+2][j:j+3]) # 3x3 칸 기준 스도쿠 만드는 과정
    if not is_correct(cells):
        return 0 # 3. 3x3 칸 기준 스도쿠 검증하기
    return 1

for t in range(1, int(input())+1):
    sudoku = [input().split() for _ in range(9)]
    print('#%s %s' % (t, validate(sudoku)))
