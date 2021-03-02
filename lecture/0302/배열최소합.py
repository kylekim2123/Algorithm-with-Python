# 세로줄(열)이 겹치지 않는지 검사
def is_possible(now_row):
    for past_row in range(now_row): # 이전 행을 순회하면서
        if check[past_row] == check[now_row]: # 열이 겹치지 않는지 검사
            return False
    return True

def dfs(row, total):
    global min_total
    if row == n:
        min_total = min(min_total, total) # 마지막 줄까지 탐색했다면, 합의 최소값을 비교
        return
    for col in range(n): # 해당 행의 모든 열 탐색
        temp = total # total을 임시 저장하지 않으면 for문을 순회하는 동안 누적되기 때문에 temp 선언
        check[row] = col # 해당 row에 어느 col을 선택했는지 기록
        if is_possible(row): # 겹치는 열이 없다면 재귀 들어간다.
            temp += numbers[row][col]
            if temp >= min_total:
                continue # Backtracking (더했는데, 이미 최소 합보다 크면 더 볼 필요 없음)
            dfs(row+1, temp) # 다음 행 이동

for t in range(1, int(input())+1):
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(n)]
    min_total = 90 # 최대 수 9, 최대 줄 10줄이므로 90보다 큰 total은 불가능
    check = [0] * n # check 리스트의 인덱스 = row , check 리스트의 값 = column
    dfs(0, 0)
    print('#%s %s' % (t, min_total))