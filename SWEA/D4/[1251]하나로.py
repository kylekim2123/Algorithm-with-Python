# 1251. 하나로

def get_dist_square(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return (x1-x2)**2 + (y1-y2)**2

def find_set(node):
    if node != p[node]:
        p[node] = find_set(p[node]) # 경로 압축
    return p[node]

for t in range(1, int(input())+1):
    n = int(input())
    nodes = list(zip(map(int, input().split()), map(int, input().split())))
    e = float(input())
    edges = sorted((get_dist_square(nodes[i], nodes[j]), i, j) for i in range(n-1)
                                                               for j in range(i+1, n))
    p = list(range(n))
    cost = 0
    for w, x, y in edges:
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root:
            p[y_root] = x_root
            cost += w
    print('#{} {:.0f}'.format(t, e * cost))