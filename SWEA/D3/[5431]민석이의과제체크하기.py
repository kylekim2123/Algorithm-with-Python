# 5431. 민석이의 과제 체크하기

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    hw = set(map(int, input().split()))
    nhw = list(set(range(1, n+1)) - hw)
    print(f'#{t}', *nhw)