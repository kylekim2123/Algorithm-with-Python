def make_burger(turn, point, cal):
    global max_point
    if cal > L or (point + future[N-turn-1]) <= max_point:
        return
    if turn >= N:
        max_point = max(max_point, point)
        return
    make_burger(turn+1, point, cal)
    make_burger(turn+1, point+scores[turn], cal+calories[turn])

for t in range(1, int(input())+1):
    N, L = map(int, input().split())
    scores, calories = [], []
    for _ in range(N):
        score, calorie = map(int, input().split())
        scores.append(score)
        calories.append(calorie)
    future = [scores[-1]]
    for i in range(N-2, -1, -1):
        future.append(future[-1] + scores[i])
    max_point = 0
    make_burger(0, 0, 0)
    print('#%s %s' % (t, max_point))
