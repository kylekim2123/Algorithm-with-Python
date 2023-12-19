class Node:
    def __init__(self, center):
        self.center = center
        self.left = None
        self.right = None

def insert(node, root):
    if node.center < root.center:
        if root.left:
            insert(node, root.left)
        else:
            root.left = node
    elif node.center > root.center:
        if root.right:
            insert(node, root.right)
        else:
            root.right = node

def find_parent(node, root):
    if root.left == node or root.right == node:
        return root
    if node.center < root.center:
        return find_parent(node, root.left)
    if node.center > root.center:
        return find_parent(node, root.right)

def delete(target, root_node):
    parent = find_parent(target, root_node)
    if target.left and target.right:
        child_parent, child = target, target.right
        while child.left:
            child_parent, child = child, child.left
        child.left = target.left
        if child_parent != target:
            child_parent.left = child.right
            child.right = target.right
        if target == root_node:
            global root
            root = child.center
        else:
            if target.center < parent.center:
                parent.left = child
            else:
                parent.right = child
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

def get_preorder(node):
    result.append(node.center)
    if node.left:
        get_preorder(node.left)
    if node.right:
        get_preorder(node.right)


v, i, d = input().split()
nodes = list(map(int, input().split()))
insertions = list(map(int, input().split()))
deletions = list(map(int, input().split()))

root = nodes[0]
bst = {root: Node(root)}
for node in nodes[1:]:
    bst[node] = Node(node)
    insert(bst[node], bst[root])
for node in insertions:
    bst[node] = Node(node)
    insert(bst[node], bst[root])
for node in deletions:
    delete(bst[node], bst[root])
    del(bst[node])

result = []
get_preorder(bst[root])
print(' '.join(map(str, result)))