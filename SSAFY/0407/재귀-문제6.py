def recursion(node, ancestors, generations):
    if node in tree:
        for i, child in enumerate(tree[node], start=1):
            recursion(child, ancestors + [node], generations + [i])
    else:
        ancestors += [node]
        rtn = f'[{str(ancestors[0]).zfill(3)}]' if not printed else '     '
        for i, ancestor in enumerate(ancestors[1:], start=1):
            if ancestor in printed:
                rtn += '   |        '
            else:
                sibling_count = len(tree[ancestors[i - 1]])
                sibling_ranking = generations[i]
                number = str(ancestor).zfill(3)

                # 유일한 자식
                if sibling_count == 1:
                    rtn += f' ----- [{number}]'
                # 첫번째 자식
                elif sibling_ranking == 1:
                    rtn += f' --+-- [{number}]'
                # 마지막 자식
                elif sibling_count == sibling_ranking:
                    rtn += f'   L-- [{number}]'
                # 그외
                else:
                    rtn += f'   +-- [{number}]'

                printed.add(ancestor)
        print(rtn)

tree = {}
edges = list(map(int, input().split()))
for i in range(0, len(edges) - 1, 2):
    tree[edges[i]] = tree.get(edges[i], []) + [edges[i + 1]]

printed = set()
recursion(edges[0], [], [1])
          #node    #anc #gen

"""
입력예제
30 54 30 2 30 45 54 1 54 3 45 123 1 101 1 102 3 103
"""

"""
출력예제 및 아이디어
printed = {30, 54, 1, 101, 102}

[030] --+-- [054] --+-- [001] --+-- [101]  # generation = [1, 1, 1, 1], ancestors = [30, 54, 1, 101]
        l           l           L-- [102]  # generation = [1, 1, 1, 2], ancestors = [30, 54, 1, 102]
        l           L-- [003] ----- [103]  # generation = [1, 1, 2, 1], ancestors = [30, 54, 2, 103]
        +-- [002]                          # generation = [1, 2], ancestors = [1, 2]
        L-- [045] ----- [123]              # generation = [1, 3, 1], ancestors = [1, 123]
"""
