def binary_search(target, l, r):
    pre_d = 0 # 이전 방향
    while l <= r:
        m = (l+r)//2 # 가운데 정하기
        if A[m] == target: # 찾으면 1 반환
            return 1
        if A[m] > target: # 왼쪽 이동
            r, d = m-1, -1 # d = -1은 왼쪽을 의미
        else: # 오른쪽 이동
            l, d = m+1, 1 # d = 1은 오른쪽을 의미
        if pre_d == d: # 이전 방향과 동일한 방향으로 또 가면 break
            break
        pre_d = d # 이전 방향을 현재 방향으로 갱신
    return 0

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    A, B = sorted(map(int, input().split())), list(map(int, input().split()))
    count = 0
    for b in B:
        count += binary_search(b, 0, N-1) # B의 모든 원소에 대해서 이진탐색 후 조건에 부합하면 +1, 하지 않으면 +0
    print('#%s %s' % (t, count))
                