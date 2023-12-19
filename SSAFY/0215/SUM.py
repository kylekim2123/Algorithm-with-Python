# sum 함수 구현
def get_sum(args):
    total = 0
    for arg in args:
        total += arg
    return total


# max 함수 구현
def get_max(*args):
    max_number = args[0] # 성분이 모두 음수일 수 있으므로, 초기값은 첫 값
    for arg in args:
        if arg > max_number:
            max_number = arg
    return max_number


# 가장 높은 합을 가지는 line의 sum 값 반환
def find_max_line(arr):
    max_total = get_sum(arr[0]) # 성분이 모두 음수일 수 있으므로, 초기값은 첫 줄의 합
    for line in arr:
        max_total = get_max(max_total, get_sum(line))
    return max_total


# 배열 90도 회전
def rotate(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


SIZE = 100
for _ in range(1, 11):
    t = int(input())
    numbers = [list(map(int, input().split())) for _ in range(SIZE)]

    row_max = find_max_line(numbers)
    row_diagonal = [numbers[i][j] for i in range(SIZE) for j in range(SIZE) if i == j]
    rotate(numbers)
    column_max = find_max_line(numbers)
    column_diagonal = [numbers[i][j] for i in range(SIZE) for j in range(SIZE) if i == j]

    # 행 기준 최대값, 열 기준 최대값, 대각선의 합들 중, max가 결과 값
    result = get_max(row_max, column_max, get_sum(row_diagonal), get_sum(column_diagonal))
    print('#%s %s' % (t, result))


