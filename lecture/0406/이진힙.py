for t in range(1, int(input())+1):
    n = int(input())
    nodes = list(map(int, input().split()))
    tree = [0]

    for node in nodes:
        tree.append(node)
        idx = tree.index(node)
        parent = idx // 2
        while idx != 1 and tree[parent] > tree[idx]:
            tree[parent], tree[idx] = tree[idx], tree[parent]
            idx = parent
            parent = idx // 2

    total, idx = 0, n // 2
    while idx > 0:
        total += tree[idx]
        idx //= 2
    print('#%s %s' % (t, total))