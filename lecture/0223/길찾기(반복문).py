# dfs를 스택과 반복문으로 구현
def dfs(start):
    stack = []
    visited = [0] * SIZE
    stack.append(start)
    while stack:
        node = stack.pop()
        if not visited[node]:
            if node == B:
                return 1
            visited[node] = 1
            for next_node in AL[node]:
                if not visited[next_node]:
                    stack.append(next_node)
    return 0


SIZE, A, B = 100, 0, 99
for _ in range(1, 11):
    t, n = map(int, input().split())
    edges = list(map(int, input().split()))
    AL = [[] for _ in range(SIZE)]
    for i in range(0, n*2-1, 2):
        AL[edges[i]].append(edges[i+1])

    print('#%s %s' % (t, dfs(A)))