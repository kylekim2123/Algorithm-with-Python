# 2806. N-Queen

count = 0 # vscode에서 이거 없으면 에러라고 인식하는데, 사실 없어도 된다.

# 유망성 검사
def is_possible(now_row):
    # 이전 row들과 겹치는 열 or 대각이 있는지 검사
    for past_row in range(now_row):
        if (check[past_row] == check[now_row]) or ((now_row-past_row) == abs(check[now_row]-check[past_row])): # 열 겹치니? or 대각 겹치니?
            return False
    return True

# 퀸 놓기
def set_queen(row):
    if row == n: # 마지막 행을 지나왔다는 것이므로 한 가지 경우가 완성된 것
        global count
        count += 1
        return
    for col in range(n): # 0번 row에서 1번열 ~ n-1번열까지 모두 한번씩 놔보고 완전탐색 go go
        check[row] = col
        if is_possible(row): # 유망성 검사를 통한 백트래킹
            set_queen(row+1) # 해당 열에 퀸 놓을 수 있으면, 다음 행으로 이동

for t in range(1, int(input())+1):
    n = int(input())
    check = [0] * n # check 배열을 1차원으로 만든 것이 굉장히 중요한 개념 (index: row, value: column)
    count = 0
    set_queen(0)
    print('#%s %s' % (t, count))
