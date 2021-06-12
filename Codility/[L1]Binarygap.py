def solution(N):
    max_length, length = 0, 0
    for digit in format(N, 'b'):
        if digit == '1':
            max_length = max(max_length, length)
            length = 0
        else:
            length += 1
    return max_length
