# 단어가 들어갈 수 있는 빈공간 찾기
def find_possible_space(arr, arr_size, word_len):
    possible_space = 0
    for line in arr: # 한 줄씩
        wall = [-1] + [i for i in range(arr_size) if line[i] == '0'] + [arr_size]
        for i in range(1, len(wall)):
            space = wall[i] - (wall[i-1]+1) # 빈 공간 = 채워진 칸 끼리의 사이 거리
            if space == word_len:
                possible_space += 1
    return possible_space


# 퍼즐을 90도 회전하기
def rotate(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [list(input().split()) for _ in range(n)]
    total_space = find_possible_space(puzzle, n, k) # 가로 기준, 단어가 들어갈 수 있는 공간
    rotate(puzzle)
    total_space += find_possible_space(puzzle, n, k) # 세로 기준, 단어가 들어갈 수 있는 공간
    print('#%s %s' % (t, total_space))
