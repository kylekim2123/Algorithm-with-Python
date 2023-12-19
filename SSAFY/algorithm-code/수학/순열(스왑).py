def perm(idx):
    if idx == r:
        print(arr[:r])
        return
    for i in range(idx, N):
        arr[idx], arr[i] = arr[i], arr[idx]
        perm(idx+1)
        arr[idx], arr[i] = arr[i], arr[idx]

arr = [1, 2, 3]
N = 3
r = 3 # 몇개를 뽑을 것인가
perm(0)
