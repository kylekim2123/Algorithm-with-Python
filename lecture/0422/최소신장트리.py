def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        x, y, w = map(int, input().split())
        edges.append((w, x, y))
    edges.sort()

    parent = list(range(n+1))
    cost = 0
    for w, x, y in edges:
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root:
            parent[y_root] = x_root
            cost += w
    print('#%s %s' % (t, cost))
        