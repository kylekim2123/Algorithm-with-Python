for t in range(1, int(input())+1):
    n = int(input())
    nodes = list(map(int, input().split()))
    tree = [0] # 1번 노드부터 시작하기 위해 0을 넣은 상태로 초기화

    for node in nodes:
        tree.append(node) # 일단 트리의 맨 끝에 넣고
        idx = tree.index(node)
        parent = idx // 2
        while idx != 1 and tree[parent] > tree[idx]: # 부모 노드의 값보다 작으면 계속 교체(최소힙은 작은 값이 위에 있기 때문)
            tree[parent], tree[idx] = tree[idx], tree[parent]
            idx = parent
            parent = idx // 2

    total, idx = 0, n // 2
    while idx > 0: # 루트 노드까지 올라가면서 조상을 모두 더함
        total += tree[idx]
        idx //= 2
    print('#%s %s' % (t, total))