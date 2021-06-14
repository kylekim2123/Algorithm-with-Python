def solution(A):
    i, A = 1, set(A)
    while True:
        if i not in A:
            return i
        i += 1