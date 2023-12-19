def dfs(row, total):
    global min_total
    if row == n:
        min_total = min(min_total, total) # 마지막 줄까지 탐색했다면, 합의 최소값을 비교
        return
    for col in range(n): # 해당 행의 모든 열 탐색
        if (not visited[col]) and (total + numbers[row][col] < min_total): # backtracking
            visited[col] = True
            dfs(row + 1, total + numbers[row][col]) # 다음 행 이동
            visited[col] = False # 원상 복구

for t in range(1, int(input())+1):
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n # 열 방문 기록
    min_total = 90 # 최대 수 9, 최대 줄 10줄이므로 90보다 큰 total은 불가능
    dfs(0, 0)
    print('#%s %s' % (t, min_total))