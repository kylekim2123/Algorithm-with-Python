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


V, E = map(int, input().split()) # 정점, 간선 개수
edges = [list(map(int, input().split())) for _ in range(E)] # 간선 정보(시작, 끝)
S, G = map(int, input().split()) # 출발, 도착

# 인접 리스트
graph = [[] for _ in range(V+1)]
for start, end in edges:
    graph[start].append(end) # 단방향
    graph[end].append(start) # 양방향

stack = [] # dfs1, dfs2를 위한 스택
visited = [False] * (V+1) # 방문기록
dfs1(S)
dfs2(S)
dfs3(S)
