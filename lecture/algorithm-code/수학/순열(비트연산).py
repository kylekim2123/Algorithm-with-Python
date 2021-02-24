def perm(idx, check):
    if idx == r: # r만큼 다 뽑았다면
        print(sel) # 결과 출력
        return

    # r만큼 아직 뽑지 않았다면
    for i in range(len(arr)):
        if check & (1<<i):
            continue # i번째 원소를 이미 썼다면, 다음꺼로 넘어감
        sel[idx] = arr[i]
        perm(idx+1, check | (1<<i)) # 원상복구 필요 없음


arr = [1, 2, 3] # 원본 배열
r = 3 # 뽑을 숫자
sel = [0] * r # 결과 저장 리스트

perm(0, 0)
