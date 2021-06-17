def solution(A):
    MAX_INTERSECTIONS = 10**7
    left, right = [], []
    for j, radius in enumerate(A):
        left.append(j-radius)
        right.append(j+radius)
    left.sort()
    right.sort()
    intersections = 0
    j = 0
    for i in range(len(A)):
        while j < len(A) and left[j] <= right[i]:
            intersections += (j-i)
            j += 1
    return intersections if intersections <= MAX_INTERSECTIONS else -1
