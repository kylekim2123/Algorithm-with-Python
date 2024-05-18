# 골드 3

import sys

input = sys.stdin.readline


def insert(foods):
    node = root

    for food in foods:
        if food not in node:
            node[food] = {}

        node = node[food]


def print_ant_cave(node, level=0):
    floor = "--" * level

    for food, next_node in sorted(node.items()):
        print(f"{floor}{food}")
        print_ant_cave(next_node, level + 1)


n = int(input())
root = {}

for _ in range(n):
    insert(input().split()[1:])

print_ant_cave(root)
