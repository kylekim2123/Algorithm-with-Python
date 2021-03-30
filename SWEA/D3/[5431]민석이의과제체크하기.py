# 5431. 민석이의 과제 체크하기

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    nhw = sorted(set(range(1, n+1)) - set(map(int, input().split())))
    print(f'#{t}', *nhw)