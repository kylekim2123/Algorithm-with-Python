for t in range(1, int(input())+1):
    n, q = map(int, input().split())
    numbers = [0] * n
    for i in range(1, q+1):
        left, right = map(int, input().split()) # 범위 입력 받고
        for j in range(left-1, right): # 범위 만큼
            numbers[j] = i # i로 덧 씌움
    print('#%s %s' % (t, ' '.join(map(str, numbers))))