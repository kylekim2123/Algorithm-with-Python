# 최대 힙 (최대값이 루트 노드)

from heapq import heappush, heappop

for t in range(1, int(input())+1):
    n = int(input())
    heap = []
    result = [f'#{t}'] # 출력되는 숫자를 담는 결과 값
    for _ in range(n):
        control = list(map(int, input().split())) # 1 2 로 입력을 넣으면 2를 삽입 / 2로 입력을 넣으면 루트 노드 삭제
        if control[0] == 1:
            # 최소 힙에서 최대 힙 구현하는 방법: (우선순위, 숫자) -> 우선순위를 해당 숫자의 음수값으로 넣어서 최대 값의 우선순위를 높인다.
            heappush(heap, (-control[1], control[1]))
            continue
        if len(heap) == 0:
            result.append(-1)
            continue
        result.append(heappop(heap)[1])
    print(*result)