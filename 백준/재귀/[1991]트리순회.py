# 1991. 트리 순회 (실버1)

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, center, left, right):
        self.center = center
        self.left = left
        self.right = right

def get_preorder(vertex):
    node = tree[vertex]
    result1.append(node.center)
    if node.left != '.':
        get_preorder(node.left)
    if node.right != '.':
        get_preorder(node.right)

def get_inorder(vertex):
    node = tree[vertex]
    if node.left != '.':
        get_inorder(node.left)
    result2.append(node.center)
    if node.right != '.':
        get_inorder(node.right)

def get_postorder(vertex):
    node = tree[vertex]
    if node.left != '.':
        get_postorder(node.left)
    if node.right != '.':
        get_postorder(node.right)
    result3.append(node.center)

n = int(input())
tree = {}
for _ in range(n):
    c, l ,r = input().split()
    tree[c] = Node(c, l, r)
result1, result2, result3 = [], [], []
get_preorder('A')
get_inorder('A')
get_postorder('A')
print(''.join(result1))
print(''.join(result2))
print(''.join(result3))