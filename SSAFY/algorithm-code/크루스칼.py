# 특정 원소가 속한 집합 찾기 (루트 노드 찾기)
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node]) # 경로 압축
    return parent[node]

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        x, y, w = map(int, input().split())
        edges.append((w, x, y))
    edges.sort() # 최소 비용의 간선부터 차례로 검사

    parent = list(range(n+1))
    cost = 0
    count = 0
    # kruskal - 최소 비용 간선부터 차례로 보면서, 같은 집합이 아닌 노드들을 집합으로 묶고 최소 비용 계산
    for w, x, y in edges:
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root: # 사이클이 발생하지 않은 경우
            parent[y_root] = x_root # union
            cost += w # 비용 합
            count += 1
            if count >= n-1: # edge의 최대 수는 n-1이므로 이때 break
                break
    print('#%s %s' % (t, cost))
        