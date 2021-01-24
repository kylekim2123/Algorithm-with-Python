# 1974. 스도쿠 검증

# 줄 혹은 칸에 1~9가 정상적으로 들어있는지 판별
def validate_line(sudoku):
    for line in sudoku:
        if len(set(line)) != 9:
            return False
    return True

# row 중심의 스도쿠를 column 중심의 스도쿠로 변경 (세로줄 판별 목적)
def change_standard_of_row_to_column(sudoku):
    changed_sudoku = [list() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            changed_sudoku[j].append(sudoku[i][j])
    return changed_sudoku

# row 중심의 스도쿠를 square 중심의 스도쿠로 변경 (각 3x3 칸 판별 목적)
def change_standard_of_row_to_square(sudoku):
    changed_sudoku = [list() for _ in range(9)]
    print(changed_sudoku)
    for i in range(0, 9, 3):
        changed_sudoku[i] = sudoku[i][0:3] + sudoku[i + 1][0:3] + sudoku[i + 2][0:3]
        changed_sudoku[i + 1] = sudoku[i][3:6] + sudoku[i + 1][3:6] + sudoku[i + 2][3:6]
        changed_sudoku[i + 2] = sudoku[i][6:9] + sudoku[i + 1][6:9] + sudoku[i + 2][6:9]
    return changed_sudoku

# 스도쿠 입력 받고 정상인지 판별 (메인)
for t in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    column_sudoku = change_standard_of_row_to_column(sudoku)
    square_sudoku = change_standard_of_row_to_square(sudoku)
    if validate_line(sudoku) and validate_line(column_sudoku) and validate_line(square_sudoku):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')