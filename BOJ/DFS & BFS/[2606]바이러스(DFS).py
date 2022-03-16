# 2606. 바이러스 (실버3) - DFS


def dfs(node):
    global total
    visited[node] = True
    total += 1
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
total = -1  # 1번 컴퓨터는 제외해야 하므로 -1로 초기화

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

dfs(1)
print(total)
