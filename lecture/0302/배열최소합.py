def is_possible(now_row):
    for past_row in range(now_row):
        if check[past_row] == check[now_row]:
            return False
    return True

def dfs(row, total):
    global min_total
    if row == n:
        min_total = min(min_total, total)
        return
    for col in range(n):
        temp = total
        check[row] = col
        if is_possible(row):
            temp += numbers[row][col]
            if temp >= min_total:
                continue
            dfs(row+1, temp)

for t in range(1, int(input())+1):
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(n)]
    min_total = 90 # 최대 수 9, 최대 줄 10줄이므로 90보다 큰 total은 불가능
    check = [0] * n
    dfs(0, 0)
    print('#%s %s' % (t, min_total))