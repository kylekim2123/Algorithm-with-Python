# 4012. 요리사

from itertools import combinations

for t in range(1, int(input())+1):
    n = int(input())
    S = [list(map(int, input().split())) for _ in range(n)]
    foods = set(range(n))
    result = 987654321
    for case in combinations(foods, n//2):
        A, B = 0, 0
        for pair in combinations(case, 2):
            A += (S[pair[0]][pair[1]] + S[pair[1]][pair[0]])
        for pair in combinations(foods-set(case), 2):
            B += (S[pair[0]][pair[1]] + S[pair[1]][pair[0]])
        result = min(result, abs(A-B))
    print('#%s %s' % (t, result))