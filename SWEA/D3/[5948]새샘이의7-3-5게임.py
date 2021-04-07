# 5948. 새샘이의 7-3-5 게임

from itertools import combinations

for t in range(1, int(input())+1):
    result = sorted({sum(case) for case in combinations(map(int, input().split()), 3)}, reverse=True)[4]
    print(f'#{t} {result}')