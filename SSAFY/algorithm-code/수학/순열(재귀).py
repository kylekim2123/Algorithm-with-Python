def perm(idx):
    if idx == r: # r만큼 다 뽑았다면
        print(sel) # 결과 출력
        return

    # r만큼 아직 뽑지 않았다면
    for i in range(len(arr)):
        if check[i] == 0: # 뽑지 않은 것에 대해
            sel[idx] = arr[i] # 결과에 저장하고
            check[i] = 1 # 뽑았다고 체크하고
            perm(idx+1) # 다음 원소에 대해 순열 돈다
            check[i] = 0 # 얘를 뽑지 않고도 순열을 돌아야하므로 다시 0으로 만듦


arr = [1, 2, 3, 4] # 원본 배열
r = 3 # 뽑을 숫자
sel = [0] * r # 결과 저장 리스트
check = [0] * len(arr) # 해당 원소 이미 사용했는지 체크

perm(0)

# 만약 nPn이 아니라 nPr로 뽑고 싶으면, sel의 크기를 r만큼 주고, idx == r로 하면 된다