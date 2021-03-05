def dfs(start, count, point, cal):
    if count > N or cal > L:
        return
    global max_point
    max_point = max(max_point, point)
    for i in range(start, N):
        dfs(i+1, count+1, point+scores[i], cal+calories[i])

for t in range(1, int(input())+1):
    N, L = map(int, input().split())
    scores, calories = [], []
    for _ in range(N):
        score, calorie = map(int, input().split())
        scores.append(score)
        calories.append(calorie)
    max_point = 0
    dfs(0, 0, 0, 0)
    print('#%s %s' % (t, max_point))
