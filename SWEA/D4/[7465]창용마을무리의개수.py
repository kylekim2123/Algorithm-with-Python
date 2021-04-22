# 7465. 창용 마을 무리의 개수

def find_set(x):
    while x != P[x]:
        x = P[x]
    return x

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    P = list(range(n+1))
    for _ in range(m):
        s, e = map(int, input().split())
        P[find_set(e)] = find_set(s)
    print('#%s %s' % (t, sum(i == P[i] for i in range(1, n+1))))