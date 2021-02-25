def is_correct(sudoku):
    for line in sudoku:
        if len(set(line)) < 9:
            return False
    return True

def validate(sudoku):
    if not is_correct(sudoku):
        return 0
    if not is_correct(list(zip(*sudoku))):
        return 0
    cells = []
    for i in range(0, 6, 3):
        for j in range(0, 7, 3):
            cells.append(sudoku[i][j:j+3] + sudoku[i+1][j:j+3] + sudoku[i+2][j:j+3])
    if not is_correct(cells):
        return 0
    return 1

for t in range(1, int(input())+1):
    sudoku = [input().split() for _ in range(9)]
    print('#%s %s' % (t, validate(sudoku)))
