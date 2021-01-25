# 1979. 어디에 단어가 들어갈 수 있을까

def is_include_word_in_line(word, line):
    index = 0
    count = 0
    position = 0
    while index < len(line):
        if line[index] == 1:
            count += 1
        else:
            if count == len(word):
                position += 1
            count = 0
        if (index == len(line) - 1) and (count == len(word)):
            position += 1
        index += 1
    return position
        
def validate_line(square, word):
    count = 0
    for line in square:
        count += is_include_word_in_line(word, line)
    return count

def change_standard_of_row_to_column(square, n):
    changed_square = [list() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            changed_square[j].append(square[i][j])
    return changed_square

for t in range(1, int(input()) + 1):
    nk = list(map(int, input().split()))
    square = [list(map(int, input().split())) for _ in range(nk[0])]
    word = [1] * nk[1]
    changed_square = change_standard_of_row_to_column(square, nk[0])
    print(f'#{t} {validate_line(square, word) + validate_line(changed_square, word)}')
    