# 1215. S/W 문제해결 기본 3일차 - 회문1

def get_column_arrays(arrays):
    column_arrays = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            column_arrays[i][j] = arrays[j][i]
    return column_arrays

def count_palindrome(arrays, length):
    count = 0
    for i in range(8):
        for j in range(9 - length):
            word = arrays[i][j:j+length]
            if word == list(reversed(word)):
                count += 1
    return count

for t in range(1, 11):
    length = int(input())
    arrays = []
    for _ in range(8):
        arrays.append(list(input()))
    column_arrays = get_column_arrays(arrays)
    total = count_palindrome(arrays, length) + count_palindrome(column_arrays, length)
    print(f'#{t} {total}')
    