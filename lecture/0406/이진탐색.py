def get_inorder(node):
    if node * 2 <= n:
        get_inorder(node*2)
    global count
    tree[node] = count
    count += 1
    if node * 2 + 1 <= n:
        get_inorder(node*2+1)

for t in range(1, int(input())+1):
    n = int(input())
    tree = [0] * (n+1)
    count = 1
    get_inorder(1)
    print('#%s %s %s' % (t, tree[1], tree[n//2]))