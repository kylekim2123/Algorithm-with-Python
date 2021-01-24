# 1961. 숫자 배열 회전

def turn_90_degree(n, cube):
    turned_cube = []
    for i in range(n):
        column_line = [str(cube[j][i]) for j in range(n - 1, -1, -1)]
        turned_cube.append(column_line)
    return turned_cube


for t in range(1, int(input()) + 1):
    n = int(input())
    cube = [list(map(int, input().split())) for _ in range(n)]

    degree_90 = turn_90_degree(n, cube)
    degree_180 = turn_90_degree(n, degree_90)
    degree_270 = turn_90_degree(n, degree_180)

    print(f'#{t}')
    for i in range(n):
        print(''.join(degree_90[i]), end=' ')
        print(''.join(degree_180[i]), end=' ')
        print(''.join(degree_270[i]))
