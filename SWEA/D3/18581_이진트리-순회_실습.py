# D3

# 전위 순회 (루트 -> 왼쪽 -> 오른쪽)
def preorder(node):
    if node == -1:
        return

    pre_result.append(node)
    preorder(tree[node][0])
    preorder(tree[node][1])


# 중위 순회 (왼쪽 -> 루트 -> 오른쪽)
def inorder(node):
    if node == -1:
        return

    inorder(tree[node][0])
    in_result.append(node)
    inorder(tree[node][1])


# 후위 순회 (왼쪽 -> 오른쪽 -> 루트)
def postorder(node):
    if node == -1:
        return

    postorder(tree[node][0])
    postorder(tree[node][1])
    post_result.append(node)


v = int(input())
nodes = list(map(int, input().split()))
tree = [[-1, -1] for _ in range(v + 1)]

for i in range(0, len(nodes), 2):
    parent, child = nodes[i], nodes[i + 1]
    if tree[parent][0] == -1:
        tree[parent][0] = child
    else:
        tree[parent][1] = child

pre_result, in_result, post_result = [], [], []  # 순회 결과 저장용 리스트

preorder(1)
inorder(1)
postorder(1)

print(" ".join(map(str, pre_result)))
print(" ".join(map(str, in_result)))
print(" ".join(map(str, post_result)))
