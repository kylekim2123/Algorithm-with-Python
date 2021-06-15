def solution(X, A):
    temp = sorted(enumerate(A), key=lambda x: x[1])
    leaves = set()
    result = 0
    for k, position in temp:
        if position in leaves:
            continue
        result = max(result, k)
        leaves.add(position)
        if len(leaves) == X and position == X:
            return result
    return -1
            

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))