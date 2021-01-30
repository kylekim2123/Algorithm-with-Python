# 1220. S/W 문제해결 기본 5일차 - Magnetic

def get_column_arrays(arrays):
    column_arrays = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            column_arrays[i][j] = arrays[j][i]
    return column_arrays

for t in range(1, 11):
    length = int(input())
    square = get_column_arrays([list(map(int, input().split())) for _ in range(100)])
    total = 0
    for line in square:
        count = 0
        standard = 0
        for number in line:
            if number == 1 and standard == 0:
                standard = 1
            elif number == 2 and standard == 1:
                count += 1
                standard = 0
        total += count
    print(f'#{t} {total}')