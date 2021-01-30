# S/W 문제해결 기본 3일차 - 회문2

def get_column_arrays(arrays):
    column_arrays = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            column_arrays[i][j] = arrays[j][i]
    return column_arrays

def length_palindrome(arrays, word_length):
    max_length = word_length
    while word_length <= 100:
        break_loop = False
        for i in range(100):
            for j in range(101 - word_length):
                word = arrays[i][j:j+word_length]
                if word == list(reversed(word)):
                    max_length = word_length
                    break_loop = True
                    break
            if break_loop:
                break
        word_length += 1
    return max_length

for _ in range(1, 11):
    t = int(input())
    arrays = []
    for _ in range(100):
        arrays.append(list(input()))
    column_arrays = get_column_arrays(arrays)

    arrays_max_length = length_palindrome(arrays, 1)
    column_arrays_max_length = length_palindrome(column_arrays, arrays_max_length)
    print(f'#{t} {max(arrays_max_length, column_arrays_max_length)}')