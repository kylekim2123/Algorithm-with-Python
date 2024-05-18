# 플래티넘 4

import sys

input = sys.stdin.readline


class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root

        for char in word:
            index = ord(char) - 97

            if not node.children[index]:
                node.children[index] = Node()

            node = node.children[index]

        node.is_leaf = True

    def count(self, word):
        node = self.root.children[ord(word[0]) - 97]
        counts = 1

        for char in word[1:]:
            index = ord(char) - 97

            for i, next_node in enumerate(node.children):
                if i != index and (next_node or node.is_leaf):
                    counts += 1
                    break

            node = node.children[index]

        return counts


while True:
    try:
        words = [input().rstrip() for _ in range(int(input()))]
        trie = Trie()
        total_count = 0

        for word in words:
            trie.insert(word)

        total_count = sum(trie.count(word) for word in words)
        print(f"{total_count / len(words):.2f}")

    except ValueError:
        break
