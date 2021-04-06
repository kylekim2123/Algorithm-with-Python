def get_inorder(node):
    if node * 2 <= n:
        get_inorder(node*2) # 왼쪽 노드 갈 수 있으면 감
    global count
    tree[node] = count  # 왼쪽 자식 노드 값들 모두 부여하고 나서, 자기 자신의 값 부여
    count += 1
    if node * 2 + 1 <= n:
        get_inorder(node*2+1) # 오른쪽 노드 갈 수 있으면 감

for t in range(1, int(input())+1):
    n = int(input())
    tree = [0] * (n+1)
    count = 1
    get_inorder(1)
    print('#%s %s %s' % (t, tree[1], tree[n//2]))