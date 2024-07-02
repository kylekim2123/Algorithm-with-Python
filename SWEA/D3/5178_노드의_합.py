# D3

def postorder(node):
    if node > n:
        return  # 최대 노드 번호를 넘어가면 return

    # 완전 이진 트리의 특성을 이용한 부모와 왼쪽/오른쪽 자식 노드 구하기
    parent = node // 2
    left = node * 2
    right = left + 1  # (node * 2) + 1

    postorder(left)
    postorder(right)

    tree[parent] += tree[node]  # 현재 노드의 값을 부모 노드에 더하기


t = int(input())

for test_case in range(1, t + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)

    for _ in range(m):
        leaf, number = map(int, input().split())
        tree[leaf] = number

    postorder(1)  # 루트 노드 기준 후위 순회

    print(f"#{test_case} {tree[l]}")
