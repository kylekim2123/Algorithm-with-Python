# 플래티넘 3

import sys

input = sys.stdin.readline


def insert(word):
    node = root

    for char in word:
        if char not in node:
            node[char] = {}

        node = node[char]

    node["is_leaf"] = True


def search(word):
    node = root

    for i, char in enumerate(word):
        if char not in node:
            return False

        node = node[char]

        if "is_leaf" in node and word[i + 1:] in nicknames:
            return True

    return False


c, n = map(int, input().split())
root = {}

for _ in range(c):
    insert(input().rstrip())

nicknames = {input().rstrip() for _ in range(n)}

for _ in range(int(input())):
    print("Yes" if search(input().rstrip()) else "No")
