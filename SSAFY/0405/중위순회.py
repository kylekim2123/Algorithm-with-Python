def get_inorder(node):
    left, right = node[1], node[2]
    if left:
        get_inorder(tree[left])
    result.append(node[0])
    if right:
        get_inorder(tree[right])


for t in range(1, 11):
    n = int(input())
    tree = [['', 0, 0] for _ in range(n+1)]
    for _ in range(n):
        line = input().split()
        node = int(line[0])
        for idx, data in enumerate(line[1:]):
            if data.isdecimal():
                data = int(data)
            tree[node][idx] = data
    result = []
    get_inorder(tree[1])
    print('#%s %s' % (t, ''.join(result)))
