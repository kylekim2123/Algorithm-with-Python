# 루트 노드 찾기 (어떤 집합에 속해있는지 찾기)
def find_set(x):
    while x != P[x]:
        x = P[x]
    return x

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    P = list(range(n+1)) # 부모 노드를 저장하는 리스트
    for _ in range(m):
        s, e = map(int, input().split())
        P[find_set(e)] = find_set(s) # union
        
    # "자신 == 부모" 인 경우는 루트노드라는 뜻이므로, 루트 노드의 갯수를 세면 곧 집합의 개수
    print('#%s %s' % (t, sum(i == P[i] for i in range(1, n+1))))