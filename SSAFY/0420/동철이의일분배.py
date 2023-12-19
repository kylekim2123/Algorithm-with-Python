def choice(depth, total):
    global max_total
    if depth >= n: # depth가 끝까지 왔으면
        max_total = max(max_total, total) # 최대 확률 비교해서 갱신하기
        return
    for i in range(n):
        next_total = total * p[depth][i] # 확률 합산하기
        if not is_chosen[i] and next_total > max_total: # 선택되지 않은 업무이고, 현재까지의 확률이 최대 확률보다 클 경우
            is_chosen[i] = 1 # 업무 선택
            choice(depth+1, next_total) # 다음 단계로 재귀
            is_chosen[i] = 0 # 업무 선택 취소

for t in range(1, int(input())+1):
    n = int(input())
    p = [list(map(lambda x: float(x)/100.0, input().split())) for _ in range(n)] # map을 이용해 미리 모든 원소 100으로 나누기
    is_chosen = [0] * n # 업무 선택 여부 저장하는 리스트
    max_total = 0
    choice(0, 1)
    print('#{} {:.6f}'.format(t, max_total*100.0))
