for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    # sort를 하면 greedy하게 문제를 해결할 수 있다.
    wi = sorted(map(int, input().split()))
    tj = sorted(map(int, input().split()))
    i, j, total_weight = n-1, m-1, 0 # 뒤에서 부터 인덱스로 접근
    while i >= 0 and j >= 0:
        if wi[i] <= tj[j]: # 트럭이 해당 화물을 담을 수 있다면
            total_weight += wi[i] # 담는다
            j -= 1 # 다음 트럭으로 이동
        i -= 1 # 트럭이 담든 못담든, 다음 화물로 이동
    print('#%s %s' % (t, total_weight))