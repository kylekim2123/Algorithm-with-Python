def make_burger(turn, point, cal):
    global max_point
    if point + future[N-turn-1] <= max_point: # 미래 정보를 이용해 예측 했을 때 유망성이 없다면 진입 X
        return
    if turn >= N: # 길이를 초과하면 햄버거 점수를 비교하여 최대 점수 갱신
        max_point = max(max_point, point)
        return
    if cal + calories[turn] <= L:
        make_burger(turn+1, point+scores[turn], cal+calories[turn]) # 칼로리가 넘을 것 같지 않으면 해당 재료 사용 O
    make_burger(turn + 1, point, cal) # 칼로리가 넘을 것 같으면 해당 재료 사용 X

for t in range(1, int(input())+1):
    N, L = map(int, input().split())
    scores, calories = [], []
    for _ in range(N):
        score, calorie = map(int, input().split())
        scores.append(score)
        calories.append(calorie)
    future = [scores[-1]] # 가지치기 2를 위한 미래 정보
    for i in range(N-2, -1, -1):
        future.append(future[-1] + scores[i]) # 뒤에서 부터 더해나감
    max_point = 0
    make_burger(0, 0, 0)
    print('#%s %s' % (t, max_point))
