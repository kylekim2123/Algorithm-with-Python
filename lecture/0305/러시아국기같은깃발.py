# 중복순열과 백트래킹 문제 + 누적합
# 어느 줄을 흰, 파, 빨로 칠할 것인지 확인하는 방법은 중복순열 사용
# 중복순열 중 유망성이 없는 것들은 백트래킹으로 미리 제거
# 줄을 선택하고 바꿀 칸을 더하는 과정은 직접 for문을 하나씩 돌면서 1을 더하는 방식도 가능하나
# 각 색깔 별로 누적합 배열을 만들어서 사용하면 더 효율적이다.

# 누적합 구하기 - 각 줄에서 W, B, R이 아닌 것들을 센다.
def prefix_sum():
    not_W, not_B, not_R = [m - colors[0].count('W')], [m - colors[0].count('B')], [m - colors[0].count('R')]
    for i in range(1, n):
        not_W.append(not_W[-1] + (m - colors[i].count('W')))
        not_B.append(not_B[-1] + (m - colors[i].count('B')))
        not_R.append(not_R[-1] + (m - colors[i].count('R')))
    return not_W, not_B, not_R

# 중복 순열
def perm_repetition(depth, lines):
    if lines > n:
        return
    if depth == 3: # 세 가지 색깔의 줄 수를 정했고
        if lines == n: # 줄 수가 행 수와 같으면
            p1 = cases[0] - 1 # 1을 빼는 이유는, 1개 줄을 선택했다면 누적합 배열의 인덱스에서는 0번째 이기 때문이다.
            p2 = p1 + cases[1]
            count = (not_W[p1] + (not_B[p2]-not_B[p1]) + (not_R[-1]-not_R[p2])) # 누적합으로 각 색깔마다 바꿔야하는 칸 수 더함
            global min_count
            min_count = min(min_count, count) # 최소 합 갱신
        return
    for i in range(1, n-1): # 중복으로 뽑기 위함. (n-1인 이유는 자기 색깔을 제외한 나머지 색깔들이 각각 1줄씩 최소 2줄은 있어야 하기 때문)
        cases[depth] = i
        perm_repetition(depth+1, lines+i)

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    colors = [list(input()) for _ in range(n)]
    not_W, not_B, not_R = prefix_sum()
    cases = [0] * 3 # 중복 순열 경우의 수
    min_count = 987654321
    perm_repetition(0, 0)
    print('#%s %s' % (t, min_count))
