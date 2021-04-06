def sum_postorder(node):
    if not tree[node]:
        left, right = sum_postorder(node*2), 0
        if node*2+1 <= n:
            right = sum_postorder(node*2+1)
        tree[node] = left + right
    return tree[node]

for t in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    for _ in range(m):
        i, value = map(int, input().split())
        tree[i] = value
    sum_postorder(1)
    print('#%s %s' % (t, tree[l]))