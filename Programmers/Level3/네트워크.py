# Level 3: 네트워크

def solution(n, computers):
    visited = [False] * n
    
    def dfs(node):
        for next_node in range(n):
            if node != next_node and computers[node][next_node] and not visited[next_node]:
                visited[next_node] = True
                dfs(next_node)

    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
