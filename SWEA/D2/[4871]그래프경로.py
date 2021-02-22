# 4871. 그래프 경로(DFS)

# 풀이1. stack과 반복문으로 작성1 - stack에 일단 다 넣고 꺼내기
def dfs1(v):
    stack.append(v)
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for next_node in graph[node]:
                if not visited[next_node]:
                    stack.append(next_node)

# 풀이2. stack과 반복문으로 작성2
def pop():
    if stack:
        return stack.pop()
    return

def dfs2(v):
    visited[v] = True
    while v:
        for w in graph[v]:
            if not visited[w]:
                next_node = w
                break
        while not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)
            for w in graph[next_node]:
                if not visited[w]:
                    next_node = w
                    break
        v = pop()

# 풀이3. 재귀
def dfs3(v):
    visited[v] = True
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs3(next_node)

# 테스트 케이스
for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for start, end in edges:
        graph[start].append(end)

    stack = []
    visited = [False for _ in range(V+1)]
    dfs3(S)
    if visited[G]:
        print('#%s 1' % t)
    else:
        print('#%s 0' % t)
