# 플래티넘 1

import sys
from collections import deque

input = sys.stdin.readline

# 클래스 대신 리스트를 길게 만들어서, 별도의 공간을 할당하기 위한 상수를 정의한다.
ROOT = 26
LEAF = 27
FAIL_NODE = 28
LENGTH = 29
CHILDREN_SIZE = 26
WHOLE_SIZE = 30
STEP = 30  # 메모리 초과 방지를 위한 구간 설정


def insert(word):
    node = root

    for char in word:
        index = ord(char) - 97

        if node[index] is None:
            next_node = [None] * WHOLE_SIZE
            next_node[LENGTH] = node[LENGTH] + 1
            next_node[FAIL_NODE] = node
            node[index] = next_node

        node = node[index]

    node[LEAF] = True


def make_failure_table():
    queue = deque([root])

    while queue:
        node = queue.popleft()

        for i in range(CHILDREN_SIZE):
            next_node = node[i]

            if next_node is None:
                continue

            if node[ROOT]:
                next_node[FAIL_NODE] = root
            else:
                fail_node = node[FAIL_NODE]

                while not fail_node[ROOT] and fail_node[i] is None:
                    fail_node = fail_node[FAIL_NODE]

                if fail_node[i] is not None:
                    fail_node = fail_node[i]

                next_node[FAIL_NODE] = fail_node

            # 보통 "실패 노드"가 리프 노드이면 "원래 노드"가 리프 노드가 아니어도 리프 노드 처리를 하는데
            # 해당 문제에서는 "실패 노드"와 "원래 노드"가 동시에 리프 노드인 경우 문제가 발생한다. (잘못 개수를 셈)
            # 따라서 "원래 노드"가 리프 노드가 아닌 경우에만 "실패 노드"의 length로 갱신을 해야한다.
            # 예를 들어, abab에 대해 b와 ab가 있다고 하면 "원래 노드" ab는 2이지만, "실패 노드" b 때문에 1처리가 되어 개수가 잘못 세진다.
            if not next_node[LEAF] and next_node[FAIL_NODE][LEAF]:
                next_node[LEAF] = True
                next_node[LENGTH] = next_node[FAIL_NODE][LENGTH]

            queue.append(next_node)


def search(word):
    node = root

    for i, char in enumerate(word):
        index = ord(char) - 97

        while not node[ROOT] and node[index] is None:
            node = node[FAIL_NODE]

        if node[index] is not None:
            node = node[index]

        # 리프 노드인 경우 바꿀 수 있는 타일의 수를 갱신한다.
        # bc와 abc의 경우 더 긴 abc가 bc의 경우도 포함할 수 있으므로 max를 이용해 더 긴 경우로 갱신한다.
        if node[LEAF]:
            visited[i] = max(visited[i], node[LENGTH])


n = int(input())
street = input().rstrip()
m = int(input())
tiles = [input().rstrip() for _ in range(m)]
visited = [0] * n

# 메모리 초과 방지를 위해 지정한 STEP 만큼을 뛰어넘으며 아호코라식을 실행한다.
# 메모리의 총 사용량이 아니라, 동시에 점유하는 메모리 사용량을 따지는 듯하다.
for start in range(0, m, STEP):
    root = [None] * WHOLE_SIZE
    root[ROOT] = True
    root[LENGTH] = 0

    for i in range(start, min(start + STEP, m)):
        insert(tiles[i])

    make_failure_table()
    search(street)

# visited[i]의 의미 : "(i - visited[i] + 1) 번째 부터 i 번째 까지는 타일을 교체할 수 있다."
# 따라서 visited를 거꾸로 순회하며, "(i - visited[i] + 1) ~  i" 구간에 해당하지 않는 타일 (== 교체할 수 없는 타일)을 센다. -> 이게 total
delete_count, total = 0, 0

for i in range(n - 1, -1, -1):
    # 이미 타일을 세고 있는데, 새로운 교체 길이가 나오면 더 큰걸로 남긴다.
    # 왜냐면 4만큼 줄이고 있는데, 중간에 3 정도 남았을 때 1이 새로 나온다고 해서 아무 영향이 없기 때문이다.
    # 어차피 3만큼은 계속 가야하기 때문
    delete_count = max(delete_count, visited[i])

    if delete_count > 0:
        delete_count -= 1
    else:
        total += 1

print(total)
