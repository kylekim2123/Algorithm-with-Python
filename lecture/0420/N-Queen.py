def set_queen(row):
    if row == n: # 마지막 가로 행까지 퀸을 모두 배치했다면, 경우의 수 + 1
        global count
        count += 1
        return
    for col in range(n): # 모든 열에 대해
        ld, rd = row-col+n-1, row+col # 좌대각, 우대각의 인덱스를 정함
        if not columns[col] and not left_diagonal[ld] and not right_diagonal[rd]: # 세로, 좌대각, 우대각에 퀸의 영향력이 없는 경우
            columns[col], left_diagonal[ld], right_diagonal[rd] = 1, 1, 1 # 세로, 좌대각, 우대각 퀸의 경로 기록
            set_queen(row+1) # 다음 가로 행으로 넘어감
            columns[col], left_diagonal[ld], right_diagonal[rd] = 0, 0, 0 # 세로, 좌대각, 우대각 퀸의 경로 기록 취소

for t in range(1, int(input())+1):
    n = int(input())
    count = 0
    columns, left_diagonal, right_diagonal = [0]*n, [0]*(n*2-1), [0]*(n*2-1) # "세로, 좌대각, 우대각"에 퀸이 존재하는지 여부를 담는 리스트들
    set_queen(0)
    print('#%s %s' % (t, count))