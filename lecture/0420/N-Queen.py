def set_queen(row):
    if row == n:
        global count
        count += 1
        return
    for col in range(n):
        ld, rd = row-col+n-1, row+col
        if not columns[col] and not left_diagonal[ld] and not right_diagonal[rd]:
            columns[col], left_diagonal[ld], right_diagonal[rd] = 1, 1, 1
            set_queen(row+1)
            columns[col], left_diagonal[ld], right_diagonal[rd] = 0, 0, 0

for t in range(1, int(input())+1):
    n = int(input())
    count = 0
    columns, left_diagonal, right_diagonal = [0]*n, [0]*(n*2-1), [0]*(n*2-1)
    set_queen(0)
    print('#%s %s' % (t, count))