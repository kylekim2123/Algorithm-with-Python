def solution(X, Y, D):
    i, j = divmod(Y-X, D)
    return i + bool(j)