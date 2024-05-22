# 플래티넘 2

import sys
from collections import deque

input = sys.stdin.readline


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.fail_node = None
        self.is_root = False
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.root.is_root = True

    def insert(self, word):
        node = self.root

        for char in word:
            index = ord(char) - 97

            if node.children[index] is None:
                next_node = Node()
                next_node.fail_node = node
                node.children[index] = next_node

            node = node.children[index]

        node.is_leaf = True

    def make_failure_table(self):
        node = self.root
        queue = deque([node])

        while queue:
            node = queue.popleft()

            for i, next_node in enumerate(node.children):
                if next_node is None:
                    continue

                if node.is_root:
                    next_node.fail_node = self.root
                else:
                    fail_node = node.fail_node

                    while not fail_node.is_root and fail_node.children[i] is None:
                        fail_node = fail_node.fail_node

                    if fail_node.children[i] is not None:
                        fail_node = fail_node.children[i]

                    next_node.fail_node = fail_node

                if next_node.fail_node.is_leaf:
                    next_node.is_leaf = True

                queue.append(next_node)

    def search(self, word):
        node = self.root

        for char in word:
            index = ord(char) - 97

            while not node.is_root and node.children[index] is None:
                node = node.fail_node

            if node.children[index] is not None:
                node = node.children[index]

            if node.is_leaf:
                return "YES"

        return "NO"


trie = Trie()

for _ in range(int(input())):
    trie.insert(input().rstrip())

trie.make_failure_table()

for _ in range(int(input())):
    print(trie.search(input().rstrip()))
