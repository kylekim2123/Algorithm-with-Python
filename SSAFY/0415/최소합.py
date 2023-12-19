def move(x, y, total):
    global min_total
    if total >= min_total: # 가지치기
        return
    if x == n-1 and y == n-1:
        min_total = min(min_total, total) # 목적지에 도달하면 최소합을 갱신
        return
    if y + 1 < n:
        move(x, y+1, total+numbers[x][y+1]) # 오른쪽 값을 더하면서 이동
    if x + 1 < n:
        move(x+1, y, total+numbers[x+1][y]) # 아래쪽 값을 더하면서 이동

for t in range(1, int(input())+1):
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(n)]
    min_total = 13 * 13 * 10 # 문제 조건에서 가능한 최대값으로 초기화
    move(0, 0, numbers[0][0])
    print('#%s %s' % (t, min_total))