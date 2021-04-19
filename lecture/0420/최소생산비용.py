def manufacture(count, cost):
    global min_cost
    if cost >= min_cost:
        return
    if count >= n:
        min_cost = cost
        return
    for i in range(n):
        if not product[i]:
            product[i] = 1
            manufacture(count+1, cost+v[i][count])
            product[i] = 0


for t in range(1, int(input())+1):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]
    product = [0] * n
    min_cost = 99 * n
    manufacture(0, 0)
    print('#%s %s' % (t, min_cost))