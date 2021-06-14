def solution(A):
    left, right = A[0], sum(A[1:])
    min_diff = abs(left-right)
    for i in range(1, len(A)-1):
        left += A[i]
        right -= A[i]
        min_diff = min(min_diff, abs(left-right))
    return min_diff