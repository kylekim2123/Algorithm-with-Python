# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, e):
    queue = [(s, e)]
    warehouse[s][e] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and warehouse[nx][ny]:
                queue.append((nx, ny))
                warehouse[nx][ny] = 0
    return x-s+1, y-e+1 # x, y는 행렬의 가장 오른쪽 아래 좌표. s, e는 행렬의 가장 왼쪽 위 좌표.

for t in range(1, int(input())+1):
    n = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(n)]
    matrix = []
    for i in range(n):
        for j in range(n):
            if warehouse[i][j]: # visited를 쓰지 않고 바로 warehouse 배열에서 방문 처리를 할 수 있음
                matrix.append(bfs(i, j))

    matrix.sort(key=lambda x: (x[0]*x[1], x[0])) # 행렬의 크기를 우선으로 정렬하고, 그 값이 같으면 행의 크기로 정렬
    result = [t, len(matrix)] # 한꺼번에 출력하기 위해 테스트케이스와 행렬의 갯수를 먼저 넣음
    for unit in matrix:
        result.append(unit[0])
        result.append(unit[1])
    print('#%s' % ' '.join(map(str, result)))
