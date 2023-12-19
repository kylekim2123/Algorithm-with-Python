def sum_postorder(node):
    if not tree[node]: # 리프 노드가 아니면, 즉 비어있는 부모 노드라면
        left, right = sum_postorder(node*2), 0 # 완전이진트리 특성 상, 리프노드가 아닌 노드들은 무조건 왼쪽 노드가 있다.
        if node*2+1 <= n: # 오른쪽 노드의 위치가 범위 이내라면
            right = sum_postorder(node*2+1) # 오른쪽 자식 노드도 구한다.
        tree[node] = left + right # 왼쪽 + 오른쪽 = 부모
    return tree[node] # 리프 노드이거나, 비어있지 않은 노드라면 그냥 값만 반환

for t in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    for _ in range(m):
        i, value = map(int, input().split())
        tree[i] = value # 리프 노드 먼저 저장
    sum_postorder(1) # 후위탐색으로 리프 노드들을 먼저 합해가면서 올라간다.
    print('#%s %s' % (t, tree[l]))