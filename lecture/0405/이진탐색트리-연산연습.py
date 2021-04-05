class Node:
    def __init__(self, center):
        self.center = center
        self.left = None
        self.right = None

def insert(node, root):
    root_node = bst[root]
    if node < root_node.center:
        if root_node.left:
            insert(node, root_node.left)
        else:
            bst[node] = Node(node)
            root_node.left = bst[node].center
    elif node > root_node.center:
        if root_node.right:
            insert(node, root_node.right)
        else:
            bst[node] = Node(node)
            root_node.right = bst[node].center

def find_parent(node, root):
    if bst[root].left == node or bst[root].right == node:
        return root
    if node < root:
        return find_parent(node, bst[root].left)
    if node > root:
        return find_parent(node, bst[root].right)

def delete(node):
    global root
    target = bst[node]
    parent = bst.get(find_parent(node, root))
    if target.left and target.right:
        child_parent, child = target, bst[target.right]
        while child.left:
            child_parent, child = child, bst[child.left]
        child.left = target.left
        if child_parent != target:
            child_parent.left = child.right
            child.right = target.right
        if node == root:
            root = child.center
        else:
            if target.center < parent.center:
                parent.left = child.center
            else:
                parent.right = child.center
    elif target.left or target.right:
        if target.center < parent.center:
            parent.left = (target.left or target.right)
        else:
            parent.right = (target.left or target.right)
    else:
        if target.center < parent.center:
            parent.left = None
        else:
            parent.right = None
    del(bst[node])

def get_preorder(node):
    result.append(node)
    if bst[node].left:
        get_preorder(bst[node].left)
    if bst[node].right:
        get_preorder(bst[node].right)


v, i, d = input().split()
nodes = list(map(int, input().split()))
insertions = list(map(int, input().split()))
deletions = list(map(int, input().split()))

root = nodes[0]
bst = {root: Node(root)}
for node in nodes[1:]:
    insert(node, root)
for node in insertions:
    insert(node, root)
for node in deletions:
    delete(node)

result = []
get_preorder(root)
print(' '.join(map(str, result)))