# D2

def search(parent):
    global total

    for child in tree[parent]:
        if child != -1:
            total += 1
            search(child)


t = int(input())

for test_case in range(1, t + 1):
    e, n = map(int, input().split())
    nodes = list(map(int, input().split()))
    tree = [[-1, -1] for _ in range(e + 2)]  # (left, right)

    for i in range(0, len(nodes), 2):
        parent, child = nodes[i], nodes[i + 1]

        if tree[parent][0] == -1:
            tree[parent][0] = child  # left가 비었다면 left에 할당
        else:
            tree[parent][1] = child  # right가 비었다면 right에 할당

    total = 1  # 서브트리의 루트노드 1개를 세고 시작
    search(n)

    print(f"#{test_case} {total}")
