class Node:
    def __init__(self, center):
        self.center = center
        self.left = None
        self.right = None

def create(node, root):
    root_node = bst[root]
    if node < root_node.center:
        if root_node.left:
            create(node, root_node.left)
        else:
            bst[node] = Node(node)
            root_node.left = bst[node].center
    elif node > root_node.center:
        if root_node.right:
            create(node, root_node.right)
        else:
            bst[node] = Node(node)
            root_node.right = bst[node].center

def get_preorder(node):
    result.append(node)
    if bst[node].left:
        get_preorder(bst[node].left)
    if bst[node].right:
        get_preorder(bst[node].right)

v = int(input())
nodes = list(map(int, input().split()))
root = nodes[0]
bst = {root: Node(root)}
for node in nodes[1:]:
    create(node, root)
result = []
get_preorder(root)
print('-'.join(map(str, result)))
