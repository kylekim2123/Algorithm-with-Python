def get_preorder(node):
    preorder.append(node)
    if tree[node][0]:
        get_preorder(tree[node][0])
    if tree[node][1]:
        get_preorder(tree[node][1])


def get_inorder(node):
    if tree[node][0]:
        get_inorder(tree[node][0])
    inorder.append(node)
    if tree[node][1]:
        get_inorder(tree[node][1])


def get_postorder(node):
    if tree[node][0]:
        get_postorder(tree[node][0])
    if tree[node][1]:
        get_postorder(tree[node][1])
    postorder.append(node)
    

for t in range(1, int(input())+1):
    v = int(input())
    edges = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(v+1)]
    for i in range(0, len(edges), 2):
        if tree[edges[i]][0]:
            tree[edges[i]][1] = edges[i+1]
        else:
            tree[edges[i]][0] = edges[i+1]
    preorder, inorder, postorder, root = [], [], [], edges[0]
    get_preorder(root)
    get_inorder(root)
    get_postorder(root)
    print('#%s' % t, '\n'.join('-'.join(map(str, order)) for order in [preorder, inorder, postorder]), sep='\n')
    