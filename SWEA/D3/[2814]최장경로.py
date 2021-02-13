# 2814. 최장 경로
def dfs(now_index):
    visited[now_index] = True
    max_length = 1
    for j in range(len(graph[now_index])):
        next_index = graph[now_index][j]
        if not visited[next_index]:
            max_length = max(max_length, dfs(next_index)+1)
            visited[next_index] = False
    return max_length

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [list() for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    longest_route = 0
    for i in range(1, n+1):
        visited = [False] * (n+1)
        longest_route = max(longest_route, dfs(i))
    
    print(f'#{t} {longest_route}')
