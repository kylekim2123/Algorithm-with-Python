# 1209. S/W 문제해결 기본 2일차 - Sum

def get_column_arrays(arrays):
    column_arrays = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            column_arrays[i][j] = arrays[j][i]
    return column_arrays

for _ in range(1, 11):
    t = int(input())
    arrays = []
    for _ in range(100):
        arrays.append(list(map(int, input().split())))
    column_arrays = get_column_arrays(arrays)

    max_sum = 0
    max_sum = max(max_sum, max([sum(line) for line in arrays]))
    max_sum = max(max_sum, max([sum(line) for line in column_arrays]))
    max_sum = max(max_sum, sum([arrays[i][j] for i in range(100) for j in range(100) if i == j]))
    max_sum = max(max_sum, sum([arrays[i][j] for i in range(100) for j in range(99, -1, -1) if i == 99 - j]))

    print(f'#{t} {max_sum}')
    