INF = 987654321

def shortest_node():
    index, min_value = 0, INF
    for i, value in enumerate(D):
        if not U[i] and value < min_value:
            index, min_value = i, value
    return index


def find_shortest(start):
    U[start] = True
    D[start] = 0
    for next_node, weight in graph[start]:
        D[next_node] = weight
    for _ in range(n-2):
        now = shortest_node()
        U[now] = True
        for next_node, weight in graph[now]:
            if not U[next_node]:
                D[next_node] = min(D[next_node], D[now] + weight)


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        s, e, w = input().split()
        graph[ord(s)-97].append((ord(e)-97, int(w)))

    U = [False] * n
    D = [INF] * n
    find_shortest(0)
    print('#%s %s' % (t, ' '.join(map(str, D))))