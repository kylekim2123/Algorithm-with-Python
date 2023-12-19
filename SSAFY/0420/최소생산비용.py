def manufacture(count, cost):
    global min_cost
    if cost >= min_cost: # 이미 비용이 최소 비용을 넘으면 리턴
        return
    if count >= n: # 모두 선택했을 경우, 최소 비용 갱신
        min_cost = cost
        return
    for i in range(n):
        if not product[i]: # 해당 제품 아직 선택 안했다면
            product[i] = 1 # 제품 선택
            manufacture(count+1, cost+v[i][count]) # 비용을 더하고 재귀
            product[i] = 0 # 제품 선택 취소


for t in range(1, int(input())+1):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]
    product = [0] * n # 제품 생산 여부 저장하는 리스트
    min_cost = 99 * n
    manufacture(0, 0)
    print('#%s %s' % (t, min_cost))