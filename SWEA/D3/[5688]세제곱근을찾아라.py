# 5688. 세제곱근을 찾아라

from math import ceil

for t in range(1, int(input())+1):
    n = int(input())
    three = ceil(n**(1/3))
    if three * three * three == n:
        print(f'#{t} {three}')
    else:
        print(f'#{t} -1')