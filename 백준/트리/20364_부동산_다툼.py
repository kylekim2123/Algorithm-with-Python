# 실버 1

import sys

input = sys.stdin.readline

n, q = map(int, input().split())
visited = [False] * (n + 1)  # 특정 땅을 오리가 점유했는지에 대한 기록

for _ in range(q):
    x = int(input())  # 오리가 원하는 땅 번호
    temp = x
    blocked_node = -1

    while temp > 1:  # 루트노드에 도달하면 반복 종료
        if visited[temp]:  # 만약 오리가 점유한 노드라면
            blocked_node = temp  # 해당 노드를 저장

        temp //= 2  # 완전이진트리 특성을 이용하여 부모 노드로 이동

    if blocked_node == -1:  # 만약 막히는 곳이 없다면
        visited[x] = True  # 해당 땅은 오리가 갈 수 있으므로 점유함
        print(0)
    else:  # 만약 막히는 곳이 있다면
        print(blocked_node)  # 막히는 곳을 출력
