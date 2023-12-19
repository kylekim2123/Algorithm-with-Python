def get_preorder(node):
    result.append(node)
    for next_node in tree.get(node, []):
        get_preorder(next_node)


v = input()
edges = list(map(int, input().split()))
tree, result = {}, []
for i in range(0, len(edges)-1, 2):
    node = tree.setdefault(edges[i], [])
    node.append(edges[i+1])
get_preorder(1)
print('-'.join(map(str, result)))
